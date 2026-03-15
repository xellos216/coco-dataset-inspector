from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any


class CocoDataset:
    def __init__(
        self,
        images: list[dict[str, Any]],
        annotations: list[dict[str, Any]],
        categories: list[dict[str, Any]],
    ) -> None:
        self.images = images
        self.annotations = annotations
        self.categories = categories

        self.image_by_id: dict[int, dict[str, Any]] = {}
        self.category_by_id: dict[int, dict[str, Any]] = {}
        self.annotations_by_image_id: dict[int, list[dict[str, Any]]] = defaultdict(
            list
        )

        self.image_id_counts: Counter[int] = Counter()
        self.annotation_id_counts: Counter[int] = Counter()
        self.category_id_counts: Counter[int] = Counter()
        self.category_name_counts: Counter[str] = Counter()

        self._build_indexes()

    def _build_indexes(self) -> None:
        for image in self.images:
            image_id = image.get("id")
            if isinstance(image_id, int):
                self.image_id_counts[image_id] += 1
                if image_id not in self.image_by_id:
                    self.image_by_id[image_id] = image

        for category in self.categories:
            category_id = category.get("id")
            category_name = category.get("name")

            if isinstance(category_id, int):
                self.category_id_counts[category_id] += 1
                if category_id not in self.category_by_id:
                    self.category_by_id[category_id] = category

            if isinstance(category_name, str):
                self.category_name_counts[category_name] += 1

        for annotation in self.annotations:
            annotation_id = annotation.get("id")
            image_id = annotation.get("image_id")

            if isinstance(annotation_id, int):
                self.annotation_id_counts[annotation_id] += 1

            if isinstance(image_id, int):
                self.annotations_by_image_id[image_id].append(annotation)

    @property
    def num_images(self) -> int:
        return len(self.images)

    @property
    def num_annotations(self) -> int:
        return len(self.annotations)

    @property
    def num_categories(self) -> int:
        return len(self.categories)

    def get_annotations_for_image(self, image_id: int) -> list[dict[str, Any]]:
        return self.annotations_by_image_id.get(image_id, [])

    def has_image(self, image_id: int) -> bool:
        return image_id in self.image_by_id

    def has_category(self, category_id: int) -> bool:
        return category_id in self.category_by_id

    def get_duplicate_image_ids(self) -> list[int]:
        return sorted(
            image_id for image_id, count in self.image_id_counts.items() if count > 1
        )

    def get_duplicate_annotation_ids(self) -> list[int]:
        return sorted(
            annotation_id
            for annotation_id, count in self.annotation_id_counts.items()
            if count > 1
        )

    def get_duplicate_category_ids(self) -> list[int]:
        return sorted(
            category_id
            for category_id, count in self.category_id_counts.items()
            if count > 1
        )

    def get_duplicate_category_names(self) -> list[str]:
        return sorted(
            name for name, count in self.category_name_counts.items() if count > 1
        )
