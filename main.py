from ast import arg
import os
import argparse

h_space = 0


class Generator:
    """
        This class contains functions to print or write to a file a directory hierarchy of the files.
    """

    def __init__(self, w_icons=True):
        """
            w_icons: when set to true, folder/files icons will be on the generated text. Otherwise <-> = file and <--> = folder
        """
        self.h_space = 0  # - varible to keep track on how far it goes in the folders
        self.w_icons = w_icons
        self.tokens = []  # - contains the hierarchy

    def process(self, path):
        """
            This function will go over the different files and folders and create a list of tokens in order to create the directory hierarchy
            path: Path to where to generate the directory hierarchy
        """
        for dir_option in os.listdir(path=path):
            line = ""
            for _ in range(self.h_space):
                line += '|   '
            if os.path.isfile(f'{path}{dir_option}'):
                if self.w_icons:
                    line += f'|📄 {dir_option}\n'
                else:
                    line += f"|-{dir_option}\n"
                self.tokens.append(line)
            else:
                self.h_space += 1
                if self.w_icons:
                    line += f"|📂 {dir_option}\n"
                else:
                    line += f"|--{dir_option}\n"
                self.tokens.append(line)
                self.process(f'{path}{dir_option}/')
                self.h_space -= 1
        self.tokens.append('|\n')

    def print_hierarchy(self):
        for token in self.tokens[:-1]:
            print(token, end='')

    def write_to_file(self, file_name):
        with open(file_name, 'w', encoding='utf-8') as file:
            for token in self.tokens[:-1]:
                file.write(token)

    def clear(self):
        self.tokens = []


def main(path, args):
    gen = Generator(w_icons=args["icons"])
    gen.process(path)

    gen.print_hierarchy()

    if args["output_file"]:
        gen.write_to_file(args["output_file"])


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', '--path', required=True,
                    help="Specify the path to where to generate the folder hierarchy")

    ap.add_argument('-i', '--icons', default=False, action=argparse.BooleanOptionalAction,
                    help="When set, icons of folder/files will be displayed")

    ap.add_argument('-f', '--output_file',
                    help="name/path of the desired output file")

    args = vars(ap.parse_args())
    main(args["path"], args)
