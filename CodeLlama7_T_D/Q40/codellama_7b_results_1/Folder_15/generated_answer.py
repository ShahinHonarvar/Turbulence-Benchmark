
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the characters and their ASCII values
    char_dict = {}
    for char in string:
        char_dict[char] = ord(char)
    # Sort the dictionary by key (character) and value (ASCII value)
    sorted_dict = dict(sorted(char_dict.items(), key=lambda x: (x[1], x[0]))))
    # Return the top n characters in ascending order based on their ASCII values
    return list(map(lambda x: x[0], sorted_dict.items())[:n])
