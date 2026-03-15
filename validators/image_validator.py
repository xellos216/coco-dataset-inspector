from __future__ import annotations

from pathlib import Path

from models.coco_dataset import CocoDataset


def find_annotations_with_missing_images(dataset: CocoDataset) -> list[int]:
    missing = []

    for ann in dataset.annotations:
        image_id = ann["image_id"]

        if not dataset.has_image(image_id):
            missing.append(ann["id"])

    return missing


def find_missing_image_files(dataset: CocoDataset, images_dir: str | Path) -> list[str]:
    images_path = Path(images_dir)
    missing_files: list[str] = []

    for image in dataset.images:
        file_name = image["file_name"]
        image_path = images_path / file_name

        if not image_path.exists():
            missing_files.append(file_name)

    return missing_files


def find_empty_images(dataset: CocoDataset) -> list[int]:
    empty_images: list[int] = []

    for image in dataset.images:
        image_id = image["id"]
        annotations = dataset.get_annotations_for_image(image_id)

        if len(annotations) == 0:
            empty_images.append(image_id)

    return empty_images
