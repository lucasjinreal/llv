import gzip
import json
import os
import struct
import numpy as np
from .faceframe import FaceFrame
from .poseframe import PoseFrame


def is_binary_file(file_name):
    """
    Tries to open file in text mode and read first 64 bytes. If it fails,
    we can be fairly certain, this is due to the file being binary encoded.
    Thanks Sehrii https://stackoverflow.com/a/51495076/949561 for the help.
    """
    try:
        with open(file_name, "tr") as check_file:
            check_file.read(32)
            return False
    except:
        return True


def _read_frames_json(filepath):
    with open(filepath, "r", encoding="utf-8", newline="\r\n") as f:
        recording_json = json.load(f)

        frame_count = recording_json["count"]
        frame_index = 0

        for frame_json in recording_json["frames"]:
            yield frame_json, frame_index, frame_count, frame_json["version"]
            frame_index += 1


def _read_frames_binary(filepath):
    file_size = os.path.getsize(filepath)
    with gzip.open(filepath, "rb") as file:
        (version,) = struct.unpack(">B", file.read(1))
        if version != FaceFrame.VERSION:
            raise Exception(
                f"Incompatible frame versions! Recording is at {version}, llv at {FaceFrame.VERSION}."
            )
        (frame_count,) = struct.unpack(">L", file.read(4))

        for frame_index in range(0, frame_count):
            raw_frame_size = file.read(4)
            (frame_size,) = struct.unpack(">L", raw_frame_size)
            frame_data = file.read(frame_size)

            yield frame_data, frame_index, frame_count, version

        file_pos = file.tell()
        if file_pos < file_size:
            raise Exception(
                f"Recording seems corrupted! Data after last frame! {file_pos}/{file_size}"
            )


def _read_frames_binary_pose(filepath):
    file_size = os.path.getsize(filepath)
    with gzip.open(filepath, "rb") as file:
        (version,) = struct.unpack(">B", file.read(1))
        if version != PoseFrame.VERSION:
            raise Exception(
                f"Incompatible frame versions! Recording is at {version}, llv at {PoseFrame.VERSION}."
            )
        (frame_count,) = struct.unpack(">L", file.read(4))

        for frame_index in range(0, frame_count):
            raw_frame_size = file.read(4)
            (frame_size,) = struct.unpack(">L", raw_frame_size)
            frame_data = file.read(frame_size)

            yield frame_data, frame_index, frame_count, version

        file_pos = file.tell()
        if file_pos < file_size:
            raise Exception(
                f"Recording seems corrupted! Data after last frame! {file_pos}/{file_size}"
            )


def read_frames(filepath, loop=False):
    is_binary = is_binary_file(filepath)
    keep_reading = True
    while keep_reading:
        if is_binary:
            frame_generator = _read_frames_binary(filepath)
        else:
            frame_generator = _read_frames_json(filepath)

        for frame_package in frame_generator:
            yield frame_package

        keep_reading = loop


def read_frames_pose(filepath, loop=False):
    is_binary = is_binary_file(filepath)
    keep_reading = True
    while keep_reading:
        if is_binary:
            frame_generator = _read_frames_binary_pose(filepath)
        else:
            frame_generator = _read_frames_json(filepath)

        for frame_package in frame_generator:
            yield frame_package

        keep_reading = loop