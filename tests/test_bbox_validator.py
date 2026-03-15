from parsers.coco_parser import parse_coco_json
from validators.bbox_validator import find_bboxes_outside_image, find_invalid_bbox_sizes


def test_find_invalid_bbox_sizes():
    dataset = parse_coco_json("sample_dataset/annotations.json")

    invalid = find_invalid_bbox_sizes(dataset)

    assert invalid == [105]


def test_find_bboxes_outside_image():
    dataset = parse_coco_json("sample_dataset/annotations.json")

    outside = find_bboxes_outside_image(dataset)

    assert outside == [106]
