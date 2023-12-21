 def return_n_smallest_chars(string):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_dict = {}
    for char in string:
        ascii_value = ord(char)
        ascii_dict[char] = ascii_value
    # Sort the dictionary by key (character) in ascending order
    sorted_dict = dict(sorted(ascii_dict.items(), key=lambda item: item[0]))
    # Create a list of exactly 32 characters from the sorted dictionary
    n_smallest_chars = []
    for i in range(32):
        char = list(sorted_dict)[i]
        n_smallest_chars.append(char)
    return n_smallest_chars
