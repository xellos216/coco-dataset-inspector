from __future__ import annotations

from typing import Any

from models.coco_dataset import CocoDataset

REQUIRED_ANNOTATION_KEYS = ("id", "image_id", "category_id", "bbox")


def find_duplicate_annotation_ids(dataset: CocoDataset) -> list[int]:
    return dataset.get_duplicate_annotation_ids()


def find_annotations_missing_required_fields(
    dataset: CocoDataset,
) -> list[dict[str, Any]]:
    invalid_annotations: list[dict[str, Any]] = []

    for annotation in dataset.annotations:
        missing_keys = [
            key for key in REQUIRED_ANNOTATION_KEYS if key not in annotation
        ]

        if missing_keys:
            invalid_annotations.append(
                {
                    "annotation": annotation,
                    "missing_keys": missing_keys,
                }
            )

    return invalid_annotations
