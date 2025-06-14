
def return_n_smallest_chars(string, n=68):
    # Create a dictionary to store the characters and their ASCII values
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = ord(char)

    # Sort the dictionary by value (ASCII value) in descending order
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

    # Extract the top 68 characters from the sorted dictionary and return them as a list
    smallest_chars = [char for char, _ in sorted_dict[:n]]
    return smallest_chars
