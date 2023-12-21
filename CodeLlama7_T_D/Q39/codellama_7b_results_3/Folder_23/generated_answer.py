
def return_n_greatest_chars(string):
    # Create a dictionary with the character as the key and its ASCII value as the value
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = ord(char)
    # Sort the dictionary by the ASCII values of the characters
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1])
    # Return the top 46 characters from the sorted list
    return [char for char, _ in sorted_dict][-46:]
