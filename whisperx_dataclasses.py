from dataclasses import dataclass
from pydantic import BaseModel

from typing import Dict, List, Tuple, Optional, Union, Any
import json

class MyBaseModel(BaseModel):\

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        res_dict = {}
        for k, v in d.items():
            k_ = k.replace("-", "_")
            res_dict[k_] = v
        return cls(**res_dict)
    
    @classmethod
    def from_json(cls, path: str):
        with open(path, "r") as file:
            d = json.load(file)
        
        return cls.from_dict(d)
        

class WordSegment(MyBaseModel):
    text: str
    start: float
    end: float

class WordSegmentList(MyBaseModel):
    word_segments: list[WordSegment]

class Segment(MyBaseModel):
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

class TranscribeResult(MyBaseModel):
    text: str
    segments: list[Segment]
    language: str

