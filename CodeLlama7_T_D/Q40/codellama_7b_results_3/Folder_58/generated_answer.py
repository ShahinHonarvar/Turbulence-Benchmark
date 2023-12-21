
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the character and its ASCII value
    char_dict = {}

    for char in string:
        char_dict[char] = ord(char)

    # Sort the dictionary by key (character) in descending order

    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

    # Return the top n elements from the sorted dictionary
    return [item[0] for item in sorted_dict[:n]]
