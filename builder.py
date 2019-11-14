import builder_utils
import argparse

parser = argparse.ArgumentParser(description="Build a file from chunks.")
parser.add_argument("input_folder", help="The folder where the chunks are stored.")
parser.add_argument("output_file", help="The file where the complete contents should be written.")

parser.add_argument("-v", "--verbose", help="Turn on verbose mode.", action="store_true")

args = parser.parse_args()

if args.verbose:
    verbose_func = print
else:
    verbose_func = lambda text: None
input_folder = args.input_folder
output_file = args.output_file

if not builder_utils.check_folder(input_folder):
    print("Input folder does not exists!")
else:   
    byte_arrays, chunk_size = builder_utils.read_byte_arrays_from_folder(input_folder, verbose_func)
    verbose_func("Start building from the files' contents.")
    byte_array = builder_utils.build_from_byte_arrays(byte_arrays, chunk_size)
    verbose_func("Building is done!")
    builder_utils.write_byte_array_to_file(output_file, byte_array)
    print(f"Wrote everything to {output_file}.")
