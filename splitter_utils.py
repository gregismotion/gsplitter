import os

def split_into_bytearrays(content, chunk_size):
    byte_arrays = []
    current_byte = 0
    while current_byte < len(content):
        byte_count = 0
        byte_array = []
        while byte_count < chunk_size:
            if not current_byte < len(content):
                break
            byte_array.append(content[current_byte])
            current_byte += 1
            byte_count += 1
        byte_arrays.append(bytearray(byte_array))
    return byte_arrays

def make_folder(folder, verbose_func = lambda text: None):
    verbose_func(f"Checking/making {folder}...")
    os.makedirs(os.path.abspath(folder), exist_ok=True)

def byte_arrays_to_file(byte_arrays, output_folder, file_name, verbose_func = lambda text: None):
    for idx, byte_array in enumerate(byte_arrays):
        current_file_name = f"{output_folder}/{file_name}.gchunk{idx}"
        with open(current_file_name, "wb") as fo:
            verbose_func(f"Currently writing into {current_file_name}...")
            fo.write(byte_array)

def split_file(file_name, output_folder, chunk_size, verbose_func = lambda text: None):
    with open(file_name, "rb") as f:
        verbose_func("Opened source file.")
        content = f.read()
        verbose_func("Reading the contents of the source file...")
        byte_arrays = split_into_bytearrays(content, chunk_size)
        byte_arrays_to_file(byte_arrays, output_folder, file_name, verbose_func)
