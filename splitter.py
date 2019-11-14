import splitter_utils
import argparse

sizes = {
            "B": 1,
            "KB": 1024,
            "MB": 1048576,
            "GB": 1073741824,
            "TB": 1099511627776
}

def convert_to_byte_size(size, unit):
    return size * sizes.get(unit, sizes["B"])

parser = argparse.ArgumentParser(description="Split a file into chunks.")
parser.add_argument("input", help="The file you want to split.")
parser.add_argument("output", help="The folder you want the chunks to be written.")

parser.add_argument("-v", "--verbose", help="Turn on verbose mode.", action="store_true")

parser.add_argument("-s", "--size", help="Set the chunks' size.", type=int, 
        default=1
)
parser.add_argument("-u", "--unit", help="Set the unit for the size parameter.", type=str, 
        default="B", 
        choices=sizes.keys()
)

args = parser.parse_args()

if args.verbose:
    verbose_func = print
else:
    verbose_func = lambda text: None
file_name = args.input
output_folder = args.output
chunk_size = convert_to_byte_size(args.size, args.unit)

splitter_utils.make_folder(output_folder, verbose_func)
splitter_utils.split_file(file_name, output_folder, chunk_size, verbose_func)
print("Done splitting the file into chunks!")
