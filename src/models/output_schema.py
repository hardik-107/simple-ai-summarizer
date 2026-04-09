from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass
class SummaryResult:
    title: str
    concise_summary: str
    key_points: list[str]
    keywords: list[str]
    statistics: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
