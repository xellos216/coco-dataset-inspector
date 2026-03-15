from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models.coco_dataset import CocoDataset

REQUIRED_TOP_LEVEL_KEYS = ("images", "annotations", "categories")


def parse_coco_json(annotation_path: str | Path) -> CocoDataset:
    path = Path(annotation_path)

    if not path.exists():
        raise FileNotFoundError(f"Annotation file not found: {path}")

    if not path.is_file():
        raise ValueError(f"Annotation path is not a file: {path}")

    with path.open("r", encoding="utf-8") as f:
        data: dict[str, Any] = json.load(f)

    _validate_top_level_structure(data)

    return CocoDataset(
        images=data["images"],
        annotations=data["annotations"],
        categories=data["categories"],
    )


def _validate_top_level_structure(data: dict[str, Any]) -> None:
    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in data:
            raise ValueError(f"Missing required top-level key: {key}")

    if not isinstance(data["images"], list):
        raise ValueError("'images' must be a list")

    if not isinstance(data["annotations"], list):
        raise ValueError("'annotations' must be a list")

    if not isinstance(data["categories"], list):
        raise ValueError("'categories' must be a list")
