database = 'test'

current_db = database



import sys

def find_current_file(db):
     #todo find "last file"
    return "data/" + database + ".db"
    
def main():
    db = sys.argv[1]

    current_file = find_current_file(db)
    
    f= open(current_file, "w+")
    

if __name__ == "__main__":
    main()