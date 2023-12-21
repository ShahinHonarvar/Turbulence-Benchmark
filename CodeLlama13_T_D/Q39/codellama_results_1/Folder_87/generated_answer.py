
def return_n_greatest_chars(string):
    # create a dictionary to store the characters and their ASCII values
    char_ascii = {}
    for char in string:
        char_ascii[char] = ord(char)
    
    # sort the dictionary by value in descending order
    sorted_chars = sorted(char_ascii.items(), key=lambda x: x[1], reverse=True)[:24]
    
    # return the list of characters with the greatest ASCII values
    return [char for char, _ in sorted_chars]
