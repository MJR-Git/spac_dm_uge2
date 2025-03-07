import os

def main():
    path = input("input path to text: ")
    try: 
        data = get_data(os.path.join(path))
        create_file(data)
        print("File created")
    except FileNotFoundError:
         print("File not found")
    except Exception as e:
         print(e)

def get_data(path):
    with open(path) as f: 
        return f.read()

def create_file(data):
    with open("newfile.csv", "w") as f:
            f.write(data)
    return f
    
if __name__ == "__main__":
     main()