
def return_nth_smallest_ascii(string):
    # create a dictionary to store the ASCII values of each character in the string
    ascii_values = {}
    for char in string:
        if char not in ascii_values:
            ascii_values[char] = ord(char)

    # sort the dictionary by value and return the 8th smallest value
    sorted_values = sorted(ascii_values.items(), key=lambda x: x[1])

    return sorted_values[7][0]
