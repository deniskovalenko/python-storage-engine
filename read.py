import os
import sys
from file_read_backwards import FileReadBackwards
import re

def find_current_file(db):
     #todo find "last file"
    return "data/" + db + ".db"

#improve efficiency -mmap, or use grep | tail...
def find_last_value_in_file(file, key):
    pattern = re.compile("^" + key + ",")
    key_and_delimeter_length = len(key) + 1
    with FileReadBackwards(file, encoding="utf-8") as frb:
        for line in frb:
            if pattern.match(line):
                return line[key_and_delimeter_length:]

    return "value not found"

def main():
    db = sys.argv[1]
    key = sys.argv[2]

    current_file = find_current_file(db)
    value = find_last_value_in_file(current_file, key)
    print(value)

if __name__ == "__main__":
    main()
