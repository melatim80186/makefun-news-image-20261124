"""Entry program for make.fun news-image-20261124.

Copies the pre-drawn 1024x1024 PNG in this repository to the output
directory. Standard library only, no network, deterministic: the same
bytes are written on every run.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
