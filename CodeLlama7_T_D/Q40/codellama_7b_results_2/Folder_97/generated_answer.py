
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the characters and their ASCII values
    char_dict = {}

    # Iterate over the string and add each character and its ASCII value to the dictionary
    for char in string:
        if char not in char_dict:
            char_dict[char] = ord(char)

    # Sort the dictionary by the ASCII values of the characters
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1])

    # Return the first n elements of the sorted dictionary
    return [item[0] for item in sorted_dict[:n]]
