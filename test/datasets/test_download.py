# ------------------------------------------------------------------------
# Trackers
# Copyright (c) 2026 Roboflow. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 [see LICENSE for details]
# ------------------------------------------------------------------------


from pathlib import Path

import pytest

from trackers.datasets.download import download_dataset


def test_invalid_dataset():
    with pytest.raises(ValueError):
        download_dataset(
            dataset="unknown",
            output_dir=Path("./tmp"),
        )


def test_invalid_split():
    with pytest.raises(ValueError):
        download_dataset(
            dataset="mot17",
            splits=["bad"],
            output_dir=Path("./tmp"),
        )

def test_valid_dataset():
    with pytest.raises(ValueError):
        download_dataset(
            dataset="mot17",
            output_dir=Path("./tmp"),
        )


def test_valid_split():
    with pytest.raises(ValueError):
        download_dataset(
            dataset="mot17",
            splits=["test"],
            output_dir=Path("./tmp"),
        )