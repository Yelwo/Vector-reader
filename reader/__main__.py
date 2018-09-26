from reader.reader_class import Reader


def main(input_file=None, output_file=None):
    reader = Reader(input_file, output_file)
    reader.translate_vector()


if __name__ == '__main__':
    main()



