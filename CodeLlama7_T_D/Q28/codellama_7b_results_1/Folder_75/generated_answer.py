
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 62 and 83 from the input string
    chars = string[62:83]
    # Create a list of ASCII values for each character in the extracted substring
    ascii_list = [ord(c) for c in chars]
    # Sort the ASCII value list in ascending order
    sorted_list = sorted(ascii_list)
    # Return the 9th smallest ASCII value from the sorted list
    return sorted_list[8]
