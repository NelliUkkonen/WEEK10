import os

def read_one_line(filename, line_number):
    target_line = ""
    try:
        with open(filename, "r") as file:
            empty_file = os.stat(filename).st_size == 0
            if empty_file == True:
                return "Empty file"
            for i, line in enumerate(file):
                if i == (line_number - 1):
                    target_line += line
            return target_line
    except FileNotFoundError:
        return "File not found"

if __name__ == '__main__':
    read_one_line("empty.txt", 2)
              