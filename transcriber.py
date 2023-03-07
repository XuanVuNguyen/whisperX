from typing import Optional
import torch
import whisperx
from whisperx_dataclasses import WhisperXBaseResponse


class Segment(WhisperXBaseResponse):
    id: int
    seek: int
    start: float
    end: float
    text: str
    tokens: list[int]
    temperature: float
    avg_logprob: float
    compression_ratio: float
    no_speech_prob: float
    # seg_text: list[str]


class TranscribeResult(WhisperXBaseResponse):
    text: str
    segments: list[Segment]
    language: str


class Transcriber:
    def __init__(self, model_name: str, device: Optional[str] = None):
        self.model_name = model_name
        self.device = device or "cuda" if torch.cuda.is_available() else "cpu"

        self.transcriber = whisperx.load_model(model_name, device=self.device)

    def __call__(self, audio_file: str) -> TranscribeResult:
        result_dict = self.transcriber.transcribe(audio_file)
        result = TranscribeResult.from_dict(result_dict)
        return result

