from parsers.coco_parser import parse_coco_json


def test_parse_coco_json_returns_dataset() -> None:
    dataset = parse_coco_json("sample_dataset/annotations.json")

    assert dataset.num_images == 5
    assert dataset.num_annotations == 8
    assert dataset.num_categories == 3
    assert dataset.has_image(1) is True
    assert dataset.has_image(99) is False
    assert dataset.has_category(1) is True
    assert dataset.has_category(999) is False
    assert dataset.get_duplicate_annotation_ids() == [106]
