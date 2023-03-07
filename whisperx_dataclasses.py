from dataclasses import dataclass
from pydantic import BaseModel

from typing import Dict, List, Tuple, Optional, Union, Any
import json

class WhisperXBaseResponse(BaseModel):

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