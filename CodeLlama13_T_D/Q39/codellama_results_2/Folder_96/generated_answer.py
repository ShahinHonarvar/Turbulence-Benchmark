
def return_n_greatest_chars(string):
    # Create a dictionary to store the characters and their ASCII values
    char_ascii = {}
    for char in string:
        char_ascii[char] = ord(char)
    
    # Sort the dictionary by value in descending order
    sorted_chars = sorted(char_ascii.items(), key=lambda x: x[1], reverse=True)[:20]
    
    # Create a list of characters from the sorted dictionary and return it
    return [char for char, _ in sorted_chars]
