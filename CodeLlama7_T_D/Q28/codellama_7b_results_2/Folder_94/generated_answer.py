
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the ASCII values of the characters in the string
    ascii_values = {}
    for char in string:
        if char not in ascii_values:
            ascii_values[char] = ord(char)
    # Sort the dictionary by value and return the 19th element (index 18)
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1])
    return sorted_ascii_values[18][0]
