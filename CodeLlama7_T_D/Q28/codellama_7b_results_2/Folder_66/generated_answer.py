
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_values = {}
    for char in string:
        ascii_values[char] = ord(char)
    # Sort the dictionary by value (ASCII value of each character)
    sorted_dict = sorted(ascii_values.items(), key=lambda x: x[1])
    # Get the 10th smallest ASCII value from the sorted dictionary
    nth_smallest_ascii = sorted_dict[9][1]
    return chr(nth_smallest_ascii)
