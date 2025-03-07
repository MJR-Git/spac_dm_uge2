import os

def main():
    # First the user inputs a path to the text file 
    # and the text is stored in the text variable.
    path = input("enter filepath: ")
    text = get_text(os.path.join(path))

    # The sort_list function splits the text by "," and creates a list
    # and sorts it by length and alphabetically.
    sorted_list = sort_list(text)

    # The char_count function counts the occurences of each character and returns a 
    # dictionary where character is the key and count is the value.
    char_dict = char_count(sorted_list)

    #The sort_dict function takes the char_dict and sorts it by number of occurences.
    sorted_dict = sort_dict(char_dict)
    
    print("\nPrinting list of names, sorted by length, and then alphabetically\n--------------------------------\n")
    print(sorted_list)
    print("\nNames printed\n--------------------------------\n")
    print("\nPrinting dictionary of character counts, sorted by count\n--------------------------------\n")
    print(sorted_dict)
    print("\nDictionary printed\n--------------------------------\n")
    return

def get_text(path):
    with open(path) as f:
        return f.read()

def sort_list(text):
    name_list = text.split(",")
    sort1 = sorted(name_list)
    sort2 = sorted(sort1, key=len)
    return sort2

def char_count(list):
    char_dict = {}

    for name in list:
        lc_name = name.lower()
        for char in lc_name:
            if char not in char_dict:
                char_dict[char] = 0
            char_dict[char] += 1
        
    return char_dict

def sort_dict(dict):
    sorted_list = []
    for char in dict:
        sorted_list.append({"char" : char, "num" : dict[char]})
    
    sorted_list = sorted(sorted_list, reverse=True, key=lambda x: x["num"])
    sorted_dict = {}
    for i in sorted_list:
        sorted_dict[i["char"]] = i["num"]
    return sorted_dict

if __name__ == "__main__":
    main()