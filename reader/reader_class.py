import re
import codecs


class Reader:

    def __init__(self, input_file_path=None, output_file_path=None):
        self.input = input_file_path or 'test.txt'
        self.output = output_file_path or 'test_out.txt'

    @staticmethod
    def inside(string):
        return re.findall(r'\[(.*?)\]', string)[0]

    def hex_len(self, string):
        return hex(len(self.inside(string).split(',')))[2:].rjust(2, '0').ljust(8, '0')

    def translate_vector(self):
        with open(self.input, 'r', encoding='utf-8') as in_file, open(self.output, 'wb') as out_file:
            text = in_file.read()
            text = text.split(';')
            for x in text:
                if x[0] == '[':
                    out_file.write(codecs.decode(str.encode(self.hex_len(x)), "hex"))
                    out_file.write(str.encode(self.inside(x).replace(',', ';')))
                    out_file.write(str.encode(';'))
                else:
                    out_file.write(str.encode(x + ';'))
