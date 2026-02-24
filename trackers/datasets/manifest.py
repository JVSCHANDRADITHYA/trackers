#!/usr/bin/env python
# ------------------------------------------------------------------------
# Trackers
# Copyright (c) 2026 Roboflow.
# Licensed under the Apache License, Version 2.0
# ------------------------------------------------------------------------

# NEED TO UPDATE MD5 AFTER DOWNLOAD

BASE_MOT17 = (
    "https://storage.googleapis.com/com-roboflow-marketing/trackers/datasets/mot17-v1"
)

DATASETS = {
    "mot17": {
        "description": "MOT17 benchmark dataset.",
        "splits": {
            "train": {
                "frames": {
                    "url": f"{BASE_MOT17}/mot17-train-frames.zip",
                    "md5": "e0a71c577a9a5fad5f3ae231ce9515d6",
                },
                "annotations": {
                    "url": f"{BASE_MOT17}/mot17-train-annotations.zip",
                    "md5": "9cbbbd091509a10f32ffbf8f0ce0c1c0",
                },
                "detections": {
                    "url": f"{BASE_MOT17}/mot17-train-public-detections.zip",
                    "md5": "1a72947884b10ed1fdcf431660219ffc",
                },
            },
            "val": {
                "frames": {
                    "url": f"{BASE_MOT17}/mot17-val-frames.zip",
                    "md5": "84a39980ad86e3d76246057c36eace99",
                },
                "annotations": {
                    "url": f"{BASE_MOT17}/mot17-val-annotations.zip",
                    "md5": "ce6fe5a619ab37800316f00b9aa9b321",
                },
                "detections": {
                    "url": f"{BASE_MOT17}/mot17-val-public-detections.zip",
                    "md5": "eb6fe4203d66ce0dedf5046cbcc76ad7",
                },
            },
            "test": {
                "frames": {
                    "url": f"{BASE_MOT17}/mot17-test-frames.zip",
                    "md5": "d672e7cb657c626d64b2a626e47e77af",
                },
                "detections": {
                    "url": f"{BASE_MOT17}/mot17-test-public-detections.zip",
                    "md5": "bab47eefb825cb5751e9a19b51ac5279",
                },
            },
        },
    }
}
