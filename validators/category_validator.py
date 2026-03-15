from __future__ import annotations

from models.coco_dataset import CocoDataset


def find_annotations_with_unknown_categories(dataset: CocoDataset) -> list[int]:
    unknown = []

    for annotation in dataset.annotations:
        category_id = annotation["category_id"]

        if not dataset.has_category(category_id):
            unknown.append(annotation["id"])

    return unknown
