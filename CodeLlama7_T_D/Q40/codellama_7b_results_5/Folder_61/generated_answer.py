
def return_n_smallest_chars(string, n=66):
    # create a dictionary to store the character and its ASCII value
    char_dict = {}
    for char in string:
        char_dict[char] = ord(char)
    # sort the dictionary by key (character) in ascending order
    sorted_dict = sorted(char_dict.items(), key=lambda x: x[0])
    # create a list of characters with smallest ASCII values
    smallest_chars = []
    for i in range(n):
        smallest_chars.append(sorted_dict[i][0])
    return smallest_chars
