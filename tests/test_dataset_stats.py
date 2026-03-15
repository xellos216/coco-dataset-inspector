from analyzers.dataset_stats import DatasetStats
from parsers.coco_parser import parse_coco_json


def test_dataset_statistics() -> None:
    dataset = parse_coco_json("sample_dataset/annotations.json")

    stats = DatasetStats(dataset).compute()

    assert stats["images"] == 5
    assert stats["annotations"] == 8
    assert stats["categories"] == 3
    assert stats["images_with_annotations"] == 3
    assert stats["images_without_annotations"] == 2
    assert stats["min_annotations_per_image"] == 0
    assert stats["max_annotations_per_image"] == 3
    assert stats["avg_annotations_per_image"] == 1.4
