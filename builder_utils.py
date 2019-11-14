import os
import glob
import re

def check_folder(input_folder):
    return os.path.isdir(input_folder)

def read_byte_arrays_from_folder(input_folder, verbose_func):
    files = sorted(glob.glob(f"{input_folder}/*.gchunk*"), key=natural_keys)
    byte_arrays = []
    for path in files:
        with open(path, "rb") as fs:
            byte_arrays.append(fs.read())
            verbose_func(f"{path} is being read...")
    return byte_arrays, os.path.getsize(files[0])

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

def build_from_byte_arrays(byte_arrays, chunk_size):
    new_byte_array = []
    for byte_array in byte_arrays:
        for byte in byte_array:
            new_byte_array.append(byte)
    return bytearray(new_byte_array)

def write_byte_array_to_file(output_file, byte_array):
    with open(output_file, "wb") as f:
        f.write(byte_array)
