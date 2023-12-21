
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_values = {}
    for char in string:
        ascii_values[char] = ord(char)
    # Sort the dictionary by value (ASCII code)
    sorted_dict = sorted(ascii_values.items(), key=lambda x: x[1])
    # Return the top n characters from the sorted dictionary
    return [item[0] for item in sorted_dict[:n]]
