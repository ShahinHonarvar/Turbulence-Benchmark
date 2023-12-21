
def return_nth_smallest_ascii(s):
    # Get the characters in the string between indices 47 and 70, both inclusive
    chars = s[47:71]
    # Create a list of tuples containing each character and its ASCII value
    char_ascii_list = [(char, ord(char)) for char in chars]
    # Sort the list by the second element (ASCII value)
    sorted_list = sorted(char_ascii_list, key=lambda x: x[1])
    # Return the character with the 14th smallest ASCII value in the sorted list
    return sorted_list[13][0]
