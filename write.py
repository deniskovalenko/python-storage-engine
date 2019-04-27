import sys
import os

def get_file_size_limit_bytes():
    return 100

def find_current_file(db):
     #todo find "last file"
    return "data/" + db + ".db"

def write_to_file(file_path, key, value):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        os.makedirs(directory)
    except FileExistsError:
        # directory already exists
        pass
    file = open(file_path, "a+")
    file.write(key + "," + value + "\n")
    file.close()

    
def main():
    db = sys.argv[1]
    key = sys.argv[2]
    value = sys.argv[3]

    current_file = find_current_file(db)
    write_to_file(current_file, key, value)
    
    current_file_size = os.path.getsize(current_file)
    if current_file_size > get_file_size_limit_bytes():
        #todo create another file, mark current file "readonly"
        print("size more than limit, create another file")
    

if __name__ == "__main__":
    main()
