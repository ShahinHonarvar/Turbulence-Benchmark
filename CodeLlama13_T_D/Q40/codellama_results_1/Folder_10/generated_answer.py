
def return_n_smallest_chars(string):
    chars = set(string)  # create a set of distinct characters in the string
    ascii_values = {}  # dictionary to store the ASCII values for each character
    for char in chars:
        ascii_values[char] = ord(char)  # get the ASCII value for each character

    sorted_chars = sorted(ascii_values, key=lambda x: -ascii_values[x])  # sort the characters by their ASCII values in descending order

    return [char for char in string if char in chars][:88]  # slice the list of characters to get only the first 88 smallest
