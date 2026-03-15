from __future__ import annotations

from models.coco_dataset import CocoDataset


class DatasetStats:
    def __init__(self, dataset: CocoDataset) -> None:
        self.dataset = dataset

    def compute(self) -> dict[str, int | float]:
        image_count = self.dataset.num_images
        annotation_count = self.dataset.num_annotations
        category_count = self.dataset.num_categories

        annotation_counts_for_defined_images: list[int] = []

        for image in self.dataset.images:
            image_id = image["id"]
            count = len(self.dataset.get_annotations_for_image(image_id))
            annotation_counts_for_defined_images.append(count)

        if annotation_counts_for_defined_images:
            min_ann = min(annotation_counts_for_defined_images)
            max_ann = max(annotation_counts_for_defined_images)
            images_with_annotations = sum(
                1 for count in annotation_counts_for_defined_images if count > 0
            )
            images_without_annotations = sum(
                1 for count in annotation_counts_for_defined_images if count == 0
            )
            avg_ann = sum(annotation_counts_for_defined_images) / image_count
        else:
            min_ann = 0
            max_ann = 0
            images_with_annotations = 0
            images_without_annotations = 0
            avg_ann = 0.0

        return {
            "images": image_count,
            "annotations": annotation_count,
            "categories": category_count,
            "avg_annotations_per_image": avg_ann,
            "min_annotations_per_image": min_ann,
            "max_annotations_per_image": max_ann,
            "images_with_annotations": images_with_annotations,
            "images_without_annotations": images_without_annotations,
        }
