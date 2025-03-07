import os

def main():
     path = input("input path to text: ")
     text = get_text(os.path.join(path))
     error_list = error_filter(text)
     return create_file(error_list)
   
def get_text(path):
     with open(path) as f:
          return f.read()  
     
def error_filter(text):
    lines = text.split("\n")
    error_list = list(filter(lambda x: "ERROR" in x or "WARNING" in x, lines))               
    return error_list

def create_file(list):
    lines = map(lambda x: x + "\n", list)
    with open("Error_log.txt", "w") as f:
            f.writelines(lines)
    return f
     
if __name__ == "__main__":
    main()