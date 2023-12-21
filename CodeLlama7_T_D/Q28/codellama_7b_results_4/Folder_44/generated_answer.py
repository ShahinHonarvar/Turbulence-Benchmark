
def return_nth_smallest_ascii(string):
    # Create a list of the characters in the string
    char_list = list(string)
    # Find the indices of the characters that occur between indices 20 to 30, both inclusive
    start_idx = max(char_list.index('A'), 20)
    end_idx = min(char_list.index('Z'), 30)
    # Create a list of the ASCII values of the characters between indices 20 to 30, both inclusive
    ascii_list = [ord(c) for c in char_list[start_idx:end_idx+1]]
    # Sort the list of ASCII values in ascending order
    sorted_ascii_list = sorted(ascii_list)
    # Return the character with the 8th smallest ASCII value
    return chr(sorted_ascii_list[7])
