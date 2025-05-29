# count the number of words in a text 
def word_count(text):
    num_words = len(text.split())
    return num_words

# count every character in a text
def char_count(text):
    # store result in a dictionary
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
    
def sort_char_count(char_dict):
    char_list = []
    # .items() returns a list of tuples (key, value) from the dictionary
    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})
    # can be a lambda or named function
    char_list.sort(key=lambda char: char["num"], reverse=True)
    return char_list