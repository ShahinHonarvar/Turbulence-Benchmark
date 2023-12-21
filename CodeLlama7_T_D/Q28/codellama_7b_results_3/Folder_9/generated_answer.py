
def return_nth_smallest_ascii(string):
    # Extract the characters from the string
    characters = set(string)

    # Initialize a dictionary to store the ASCII values of each character
    ascii_values = {}

    # Iterate over each character in the string and store its ASCII value in the dictionary
    for char in characters:
        ascii_values[char] = ord(char)

    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values.values())

    # Return the 20th smallest ASCII value
    return sorted_ascii_values[19]
