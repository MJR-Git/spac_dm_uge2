import os

def main():
    path = input("input path to text: ")
    try: 
        file_content = get_content(os.path.join(path))
        file_format = get_file_format(path)
        print(f"File format: {file_format}")
        create_file(file_content, file_format)
        print("File created")
    except IOError as e:
         print(e)
    except Exception as e:
         print(e)

def get_file_format(path):
    valid_formats = ("txt", "csv")
    if path[-3:] in valid_formats:
         return path[-3:]
    raise Exception("Invalid file format")

def get_content(path):
    with open(path) as f: 
        return f.read()

def create_file(file, file_format):
    with open(f"new_file.{file_format}", "w") as nf:
            nf.write(file)
    return nf
    
if __name__ == "__main__":
     main()