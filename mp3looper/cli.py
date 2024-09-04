#!/usr/bin/env python
"""Use mpg321 (default) to play all (*.mp3|*.MP3) files in given directory"""

import os
from pathlib import Path
from shutil import which
from subprocess import run


DEFAULT_MP3_EXECUTABLE = "mpg321"
MP3_EXECUTABLE = os.getenv("MP3_EXECUTABLE", DEFAULT_MP3_EXECUTABLE)
MP3_EXT = "*.[mM][pP]3"



def loop_play(directory: Path):
    print(f"directory={directory}")
    if not directory.glob(MP3_EXT):
        print(f"ERROR -- directory does NOT contain {MP3_EXT} files: {directory}")

    loop_count = 0
    while True:
        print(f"loop_count={loop_count}")
        for mp3_filepath in directory.glob(MP3_EXT):
            mp3_abspath = mp3_filepath.expanduser().resolve()
            exec_command = f"{MP3_EXECUTABLE} {mp3_abspath}"
            print(f"-- calling: {exec_command}")
            run(exec_command, shell=True)
        loop_count += 1



def filepath(v: str) -> Path:
    p = Path(v).expanduser().resolve()
    if not p.exists():
        raise ValueError(f"does not exist: {p}")
    if not p.is_dir():
        raise ValueError(f"Given Path is not a directory: {p}")
    return p


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-d", "--directory", type=filepath, help="Path to directory containing mp3 files")
    args = parser.parse_args()

    if not which(MP3_EXECUTABLE):
        parser.error(f"defined 'MP3_EXECUTABLE' ({MP3_EXECUTABLE}) not found! Install!")

    loop_play(args.directory)