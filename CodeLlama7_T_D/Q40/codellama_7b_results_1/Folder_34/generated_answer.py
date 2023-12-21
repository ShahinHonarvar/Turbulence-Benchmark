
def return_n_smallest_chars(string):
    # create a dictionary with character as key and ASCII value as value
    char_dict = {char: ord(char) for char in string}

    # sort the dictionary by value (ASCII value)
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1])

    # return the first 9 characters of the sorted dictionary
    return [char for char, _ in sorted_dict[:9]]
