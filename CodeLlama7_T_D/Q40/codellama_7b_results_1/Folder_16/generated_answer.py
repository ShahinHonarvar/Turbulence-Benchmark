
def return_n_smallest_chars(string, n):
    # Create a dictionary to store the ASCII values of each character
    ascii_values = {}
    for char in string:
        ascii_values[char] = ord(char)
    # Sort the dictionary by value (ASCII value)
    sorted_values = sorted(ascii_values.items(), key=lambda x: x[1])
    # Return the top n characters with the smallest ASCII values
    return [x[0] for x in sorted_values[:n]]
