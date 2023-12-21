
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the characters and their ASCII values
    char_dict = {}
    for char in string:
        char_dict[char] = ord(char)
    # Sort the dictionary by key (ASCII value)
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1])
    # Return the first n characters of the sorted list
    return [char for char, _ in sorted_dict[:n]]
