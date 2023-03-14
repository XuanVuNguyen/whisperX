from typing import List, Optional, Tuple, Union

import torch
from transcriber import TranscribeResult

import whisperx
from utils import init_logger
from whisperx_dataclasses import WhisperXBaseResponse


logger = init_logger("main")



class WordSegment(WhisperXBaseResponse):
    text: str
    start: float
    end: float


class AlignResult(WhisperXBaseResponse):
    word_segments: list[WordSegment]



class Aligner:
    def __init__(self, language: Optional[str] = None, device: Optional[str] = None):
        self.device = device or "cuda" if torch.cuda.is_available() else "cpu"
        self.language = language

        self.aligner, self.metadata = whisperx.load_align_model(
            language_code=language, device=self.device
        )

    def run(
        self, audio_file: str, transcribe_result: Optional[TranscribeResult] = None
    ) -> AlignResult:
        language = transcribe_result.language

        if language != self.language:
            logger.info(
                f"Language is not defined or mismatched. Initiate new align model..."
            )
            self.aligner, self.metadata = whisperx.load_align_model(
                language_code=language, device=self.device
            )
            self.language = language

        transcript = [each.__dict__ for each in transcribe_result.segments]

        res = whisperx.align(
            transcript,
            self.aligner,
            self.metadata,
            audio_file,
            device=self.device,
        )

        word_segments = res["word_segments"]

        return AlignResult(word_segments=word_segments)
