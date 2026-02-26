#!/usr/bin/env python
# ------------------------------------------------------------------------
# Trackers
# Copyright (c) 2026 Roboflow.
# Licensed under the Apache License, Version 2.0
# ------------------------------------------------------------------------

from __future__ import annotations

import sys
from pathlib import Path

from trackers.datasets.manifest import DATASETS
from trackers.utils.downloader import download_file, extract_zip


def download(
    dataset: str | None = None,
    split: str | None = None,
    content: str | None = None,
    output: str = "./data",
    list_only: bool = False,
) -> None:
    """
    Download benchmark tracking datasets.
    """

    if list_only:
        _print_available()
        return

    if dataset is None:
        sys.exit("Please specify a dataset name or use --list_only true.")

    dataset = dataset.lower()
    if dataset not in DATASETS:
        sys.exit(f"Unknown dataset: {dataset}")

    output_dir = Path(output).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    ds = DATASETS[dataset]
    splits_dict = ds["splits"]

    # Parse splits
    if split:
        splits = [s.strip() for s in split.split(",")]
    else:
        splits = list(splits_dict.keys())

    # Parse content
    if content:
        requested_content = [c.strip() for c in content.split(",")]
    else:
        requested_content = []

    for split_name in splits:
        if split_name not in splits_dict:
            sys.exit(f"Invalid split '{split_name}' for dataset '{dataset}'")

        available_content = splits_dict[split_name]

        if requested_content:
            selected_content = {
                c: available_content[c]
                for c in requested_content
                if c in available_content
            }

            missing = set(requested_content) - set(selected_content)
            if missing:
                sys.exit(
                    f"Content {missing} not available for split '{split_name}' "
                    f"in dataset '{dataset}'"
                )
        else:
            selected_content = available_content

        for kind, item in selected_content.items():
            url: str = item["url"]
            md5: str | None = item.get("md5")

            marker = output_dir / f".{dataset}-{split_name}-{kind}.complete"
            if marker.exists():
                print(f"[skip] {dataset}:{split_name}:{kind} already downloaded")
                continue

            zip_name = url.split("/")[-1]
            zip_path = output_dir / zip_name

            print(f"[download] {dataset}:{split_name}:{kind}")
            download_file(url, zip_path, md5=md5)
            extract_zip(zip_path, output_dir)

            marker.touch()


def _print_available() -> None:
    print("\nAvailable datasets:\n")
    for name, ds in DATASETS.items():
        print(f"{name}: {ds.get('description', '')}")
        for split_name, contents in ds["splits"].items():
            kinds = ", ".join(contents.keys())
            print(f"  - {split_name}: {kinds}")
        print()
