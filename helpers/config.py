from __future__ import annotations

__all__ = ("Config",)

from dataclasses import dataclass

import os

from typing import List
from dotenv import load_dotenv
from enum import Enum

load_dotenv()


class ENV(Enum):
    token = "TOKEN"
    prefix = "PREFIX"
    owner_ids = "OWNER_IDS"


@dataclass
class Config:
    token: str
    prefix: str
    owner_ids: List[int]

    @classmethod
    def from_env(cls) -> Config:
        data = {}
        for env in ENV:
            if env.value in os.environ:
                data[env.name] = os.environ[env.value]
                if env == ENV.owner_ids:
                    value = [int(i) for i in value.split(",")]

        return cls(**data)
