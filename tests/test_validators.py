from parsers.coco_parser import parse_coco_json
from validators.annotation_validator import (
    find_annotations_missing_required_fields,
    find_duplicate_annotation_ids,
)
from validators.category_validator import find_annotations_with_unknown_categories
from validators.image_validator import (
    find_annotations_with_missing_images,
    find_empty_images,
    find_missing_image_files,
)


def test_find_duplicate_annotation_ids() -> None:
    dataset = parse_coco_json("sample_dataset/annotations.json")

    duplicate_ids = find_duplicate_annotation_ids(dataset)

    assert duplicate_ids == [106]


def test_find_annotations_missing_required_fields() -> None:
    dataset = parse_coco_json("sample_dataset/annotations.json")

    invalid_annotations = find_annotations_missing_required_fields(dataset)

    assert invalid_annotations == []


def test_find_annotations_with_missing_images() -> None:
    dataset = parse_coco_json("sample_dataset/annotations.json")

    missing = find_annotations_with_missing_images(dataset)

    assert missing == [103]


def test_find_annotations_with_unknown_categories() -> None:
    dataset = parse_coco_json("sample_dataset/annotations.json")

    unknown_categories = find_annotations_with_unknown_categories(dataset)

    assert unknown_categories == [104]


def test_find_missing_image_files() -> None:
    dataset = parse_coco_json("sample_dataset/annotations.json")

    missing_files = find_missing_image_files(dataset, "sample_dataset/images")

    assert missing_files == ["image_005.jpg"]


def test_find_empty_images() -> None:
    dataset = parse_coco_json("sample_dataset/annotations.json")

    empty_images = find_empty_images(dataset)

    assert empty_images == [4, 5]
