import whisperx_dataclasses as resp
from utils import init_logger

import whisperx
import torch

from typing import Optional, Union, List, Tuple

logger = init_logger("main")

class TranscribeAligner:
    def __init__(
        self, 
        model_name: str, 
        language: Optional[str]=None,
        device: Optional[str]=None):

        self.model_name = model_name
        self.device = device or "cuda" if torch.cuda.is_available() else "cpu"
        self.language = language

        self.transcriber = whisperx.load_model(model_name, device=self.device)

        if language is not None:
            self.aligner, self.metadata = whisperx.load_align_model(language_code=language, device=self.device)
        else:
            self.aligner, self.metadata = None, None
    
    def transcribe(self, audio_file: str):
        res = self.transcriber.transcribe(audio_file)
        return resp.TranscribeResult.from_dict(res)
    
    def align(self, audio_file: str, transcribe: Optional[resp.TranscribeResult]=None):
        if transcribe is None:
            transcribe = self.transcribe(audio_file)
        language = transcribe.language
        if self.aligner is None or self.metadata is None or language != self.language:
            logger.info(f"Language is not defined or mismatched. Initiate new align model...")
            self.aligner, self.metadata = whisperx.load_align_model(language_code=language, device=self.device)
            self.language = language
        
        res = whisperx.align(transcribe.segments, self.aligner, self.metadata, audio_file, device=self.device)

        word_segments = res["word_segments"]

        return resp.WordSegmentList(word_segments=word_segments)

        


        