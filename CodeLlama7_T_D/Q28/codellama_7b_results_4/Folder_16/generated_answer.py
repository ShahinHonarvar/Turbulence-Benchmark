
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between indices 18 to 45, both inclusive
    start_index = string.find('a', 18)
    end_index = string.rfind('a', 0, 45)
    # Get the ASCII values of the characters at these indices
    ascii_values = [ord(string[i]) for i in range(start_index, end_index + 1)]
    # Return the character with the 7th smallest ASCII value among those characters in the string that occur between indices 18 to 45, both inclusive.
    return chr(sorted(ascii_values)[6]))
