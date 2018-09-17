import os
import re


def find_prefixes(filename):
    prefixes = set()
    with open("localisation/" + filename, "r") as read_file:
        for line in read_file.readlines()[1:]:
            line = line.strip()
            if len(line) > 1 and line[0] != '#':
                prefixes.add(re.search("([A-Za-z_\d]+)(\.|:)", line).group(1))
    return prefixes


if __name__ == "__main__":
    big_set = set()
    with open("localisation_index.index", "w") as outfile:
        for file in os.listdir("localisation"):
            # Run function on it
            for item in find_prefixes(file):
                outfile.write(item+"~"+file+"\n")