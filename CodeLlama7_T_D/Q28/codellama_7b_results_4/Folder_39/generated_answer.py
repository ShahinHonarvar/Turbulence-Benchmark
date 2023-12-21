
def return_nth_smallest_ascii(string):
    # Create a list of unique characters in the string
    unique_chars = set(string)
    # Initialize a dictionary to store the ASCII values of each character
    ascii_values = {}
    # Iterate over each character in the string and get its ASCII value
    for char in unique_chars:
        ascii_values[char] = ord(char)
    # Sort the dictionary by the ASCII value of each character
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1])
    # Return the 8th smallest ASCII value among the characters in the string
    return sorted_ascii_values[7][0]
