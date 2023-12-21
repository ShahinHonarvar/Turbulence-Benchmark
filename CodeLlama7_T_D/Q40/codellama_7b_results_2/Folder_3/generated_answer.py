
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the character and its ASCII value
    char_dict = {}
    for char in string:
        # If the character is already present in the dictionary, skip it
        if char in char_dict:
            continue

        # Add the character and its ASCII value to the dictionary
        char_dict[char] = ord(char)

    # Sort the dictionary by value (ASCII value) in descending order
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

    # Return the top n characters with the smallest ASCII values
    return [char for char, _ in sorted_dict[:n]]
