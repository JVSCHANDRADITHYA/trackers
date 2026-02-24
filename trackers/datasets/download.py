#!/usr/bin/env python
# ------------------------------------------------------------------------
# Trackers
# Copyright (c) 2026 Roboflow.
# Licensed under the Apache License, Version 2.0
# ------------------------------------------------------------------------

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from trackers.datasets.manifest import DATASETS
from trackers.utils.downloader import download_file, extract_zip


def download_dataset(
    *,
    dataset: str,
    splits: Iterable[str] | None = None,
    content: Iterable[str] | None = None,
    output_dir: Path,
) -> None:
    dataset = dataset.lower()
    if dataset not in DATASETS:
        raise ValueError(f"Unknown dataset: {dataset}")

    ds = DATASETS[dataset]

    if splits is None:
        splits = ds["splits"].keys()

    for split in splits:
        if split not in ds["splits"]:
            raise ValueError(f"Invalid split '{split}' for dataset '{dataset}'")

        available = ds["splits"][split]

        if content is None:
            selected = available
        else:
            selected = {}
            for c in content:
                if c not in available:
                    raise ValueError(
                        f"Content '{c}' not available for {dataset}:{split}"
                    )
                selected[c] = available[c]

        for item in selected.values():
            url = item["url"]
            md5 = item["md5"]

            zip_name = url.split("/")[-1]
            zip_path = output_dir / zip_name

            if zip_path.exists():
                continue

            download_file(url, zip_path, md5=md5)
            extract_zip(zip_path, output_dir)