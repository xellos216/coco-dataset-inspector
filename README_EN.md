# COCO Dataset Inspector

A CLI tool for inspecting and validating COCO-format datasets.

This tool parses a COCO JSON annotation file, analyzes dataset statistics, and performs multiple validation checks to detect common dataset issues such as invalid annotations, missing images, or incorrect bounding boxes.

---

## Demo

![CLI Demo](docs/cli-demo.gif)

---

## Features

### Dataset Statistics

The inspector computes useful dataset statistics:

- Total number of images
- Total number of annotations
- Number of categories
- Average annotations per image
- Minimum / maximum annotations per image
- Number of images with annotations
- Number of images without annotations

### Validation Checks

The tool performs multiple integrity checks on the dataset:

Annotation checks

- Duplicate annotation IDs
- Missing required annotation fields

Category checks

- Annotations referencing unknown categories

Image checks

- Annotations referencing missing images
- Missing image files on disk
- Images without annotations

Bounding box checks

- Invalid bounding box sizes
- Bounding boxes outside image boundaries

---

## Project Structure

```

coco-dataset-inspector/
│
├── analyzers/
│   └── dataset_stats.py
│
├── models/
│   └── coco_dataset.py
│
├── parsers/
│   └── coco_parser.py
│
├── validators/
│   ├── annotation_validator.py
│   ├── bbox_validator.py
│   ├── category_validator.py
│   └── image_validator.py
│
├── sample_dataset/
│   ├── images/
│   └── annotations.json
│
├── tests/
│
└── inspector.py

```

---

## Installation

Create a virtual environment and install dependencies.

```

python -m venv .venv
source .venv/bin/activate
pip install pytest

```

---

## Usage

Run the dataset inspector from the command line.

```

python inspector.py 
--images sample_dataset/images 
--annotations sample_dataset/annotations.json

```

Example output:

```

# COCO Dataset Inspector

## Dataset Summary

Images: 5
Annotations: 8
Categories: 3
Avg annotations per image: 1.40
Min annotations per image: 0
Max annotations per image: 3
Images with annotations: 3
Images without annotations: 2

## Validation Results

Duplicate annotation IDs: 1
Annotations missing required fields: 0
Annotations with missing image references: 1
Annotations with unknown categories: 1
Missing image files: 1
Empty images: 2
Invalid bbox sizes: 1
Bboxes outside image boundaries: 1

```

---

## Testing

Run the test suite using pytest.

```

pytest

```

---

## Example Dataset

The repository includes a small `sample_dataset` used for testing.

It intentionally contains several issues to demonstrate the validation checks:

- duplicate annotation IDs
- invalid bounding boxes
- annotations referencing missing images
- missing image files

---

## Purpose

This project demonstrates how to build a modular Python CLI tool for dataset validation using:

- structured data models
- modular validation logic
- CLI argument parsing
- automated testing with pytest

