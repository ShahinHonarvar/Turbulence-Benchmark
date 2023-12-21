
def return_n_greatest_chars(string):
    # create a dictionary with the characters as keys and their ASCII values as values
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = ord(char)
    # sort the dictionary by value (ASCII value) in descending order
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    # return the top 33 characters with the greatest ASCII values
    return [item[0] for item in sorted_dict[:33]]
