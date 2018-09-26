import argparse

from reader.reader_class import Reader


def main():
    args = parse_arguments()
    reader = Reader(args.input_file, args.output_file)
    reader.translate_vector()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file", "-i", help="input file path", type=str)
    parser.add_argument("--output_file", "-o", help="output file path", type=str)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()



