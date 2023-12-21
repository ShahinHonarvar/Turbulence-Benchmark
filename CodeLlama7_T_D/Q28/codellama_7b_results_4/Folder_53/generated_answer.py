
def return_nth_smallest_ascii(s):
    # Extract the characters between indices 40 and 60, inclusive
    sub_str = s[40:61]
    # Convert the extracted string to a list of characters
    char_list = list(sub_str)
    # Find the 19th smallest ASCII value in the list
    ascii_vals = [ord(c) for c in char_list]
    sorted_ascii_vals = sorted(ascii_vals)
    nth_smallest_ascii = sorted_ascii_vals[18]
    # Return the character with the 19th smallest ASCII value
    return chr(nth_smallest_ascii)
