__all__ = ("Config",)

from dataclasses import dataclass

from typing import List


@dataclass
class Config:
    token: str
    prefix: str
    owner_ids: List[int]
