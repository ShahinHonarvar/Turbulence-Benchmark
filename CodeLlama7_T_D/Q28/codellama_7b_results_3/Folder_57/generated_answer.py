
def return_nth_smallest_ascii(s):
    # Extract the characters between indices 17 and 34 from the input string
    sub_string = s[17:35]
    # Convert the extracted substring to a list of ASCII values
    ascii_values = [ord(char) for char in sub_string]
    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the character with the 18th smallest ASCII value among those characters that occur between indices 17 and 34, both inclusive.
    return sub_string[sorted_ascii_values.index(18)]
