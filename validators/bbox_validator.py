from __future__ import annotations

from models.coco_dataset import CocoDataset


def find_invalid_bbox_sizes(dataset: CocoDataset) -> list[int]:
    invalid = []

    for ann in dataset.annotations:
        bbox = ann["bbox"]
        width = bbox[2]
        height = bbox[3]

        if width <= 0 or height <= 0:
            invalid.append(ann["id"])

    return invalid


def find_bboxes_outside_image(dataset: CocoDataset) -> list[int]:
    outside = []

    image_map = {img["id"]: img for img in dataset.images}

    for ann in dataset.annotations:
        image_id = ann["image_id"]

        if image_id not in image_map:
            continue

        image = image_map[image_id]
        img_w = image["width"]
        img_h = image["height"]

        x, y, w, h = ann["bbox"]

        if x < 0 or y < 0 or x + w > img_w or y + h > img_h:
            outside.append(ann["id"])

    return outside
