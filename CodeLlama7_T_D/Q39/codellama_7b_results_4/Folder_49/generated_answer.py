
def return_n_greatest_chars(string, n):
    # Create a dictionary with the character as key and its ASCII value as value
    char_dict = {char: ord(char) for char in string}

    # Sort the dictionary by value in descending order
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

    # Return the top n characters from the sorted list
    return [char for char, _ in sorted_dict[:n]]
