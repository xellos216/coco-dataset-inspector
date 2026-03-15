from __future__ import annotations

import argparse
from pathlib import Path

from analyzers.dataset_stats import DatasetStats
from parsers.coco_parser import parse_coco_json
from validators.annotation_validator import (
    find_annotations_missing_required_fields,
    find_duplicate_annotation_ids,
)
from validators.bbox_validator import find_bboxes_outside_image, find_invalid_bbox_sizes
from validators.category_validator import find_annotations_with_unknown_categories
from validators.image_validator import (
    find_annotations_with_missing_images,
    find_empty_images,
    find_missing_image_files,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect and validate a COCO-format dataset."
    )
    parser.add_argument(
        "--images",
        required=True,
        help="Path to the directory containing dataset images.",
    )
    parser.add_argument(
        "--annotations",
        required=True,
        help="Path to the COCO annotations JSON file.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    images_dir = Path(args.images)
    annotations_path = Path(args.annotations)

    dataset = parse_coco_json(annotations_path)
    stats = DatasetStats(dataset).compute()

    duplicate_annotation_ids = find_duplicate_annotation_ids(dataset)
    annotations_missing_required_fields = find_annotations_missing_required_fields(
        dataset
    )
    annotations_with_missing_images = find_annotations_with_missing_images(dataset)
    annotations_with_unknown_categories = find_annotations_with_unknown_categories(
        dataset
    )
    missing_image_files = find_missing_image_files(dataset, images_dir)
    empty_images = find_empty_images(dataset)
    invalid_bbox_sizes = find_invalid_bbox_sizes(dataset)
    bboxes_outside_image = find_bboxes_outside_image(dataset)

    print("COCO Dataset Inspector")
    print("=" * 22)
    print()

    print("Dataset Summary")
    print("-" * 15)
    print(f"Images: {stats['images']}")
    print(f"Annotations: {stats['annotations']}")
    print(f"Categories: {stats['categories']}")
    print(f"Avg annotations per image: {stats['avg_annotations_per_image']:.2f}")
    print(f"Min annotations per image: {stats['min_annotations_per_image']}")
    print(f"Max annotations per image: {stats['max_annotations_per_image']}")
    print(f"Images with annotations: {stats['images_with_annotations']}")
    print(f"Images without annotations: {stats['images_without_annotations']}")
    print()

    print("Validation Results")
    print("-" * 18)
    print(f"Duplicate annotation IDs: {len(duplicate_annotation_ids)}")
    print(
        "Annotations missing required fields: "
        f"{len(annotations_missing_required_fields)}"
    )
    print(
        "Annotations with missing image references: "
        f"{len(annotations_with_missing_images)}"
    )
    print(
        "Annotations with unknown categories: "
        f"{len(annotations_with_unknown_categories)}"
    )
    print(f"Missing image files: {len(missing_image_files)}")
    print(f"Empty images: {len(empty_images)}")
    print(f"Invalid bbox sizes: {len(invalid_bbox_sizes)}")
    print(f"Bboxes outside image boundaries: {len(bboxes_outside_image)}")


if __name__ == "__main__":
    main()
