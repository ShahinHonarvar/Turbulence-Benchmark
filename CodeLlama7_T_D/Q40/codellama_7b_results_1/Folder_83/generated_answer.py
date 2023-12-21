
def return_n_smallest_chars(string):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_dict = {}
    for char in string:
        ascii_dict[char] = ord(char)
    # Sort the dictionary by value in descending order and create a list of keys (i.e., characters) from the sorted dictionary
    sorted_keys = sorted(ascii_dict, key=lambda x: ascii_dict[x], reverse=True)
    # Return the first 38 elements of the list, which are the smallest ASCII values
    return sorted_keys[:38]
