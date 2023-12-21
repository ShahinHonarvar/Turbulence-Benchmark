
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_dict = {}
    for char in string:
        ascii_value = ord(char)
        ascii_dict[ascii_value] = char
    # Sort the dictionary by key (ASCII value) in descending order
    sorted_dict = sorted(ascii_dict.items(), reverse=True)
    # Return the top n characters with the smallest ASCII values
    return [char for ascii_value, char in sorted_dict[:n]]
