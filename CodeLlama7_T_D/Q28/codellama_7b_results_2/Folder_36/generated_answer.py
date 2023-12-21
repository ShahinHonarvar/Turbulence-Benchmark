
def return_nth_smallest_ascii(string):
    # Find the indices of the characters that occur between indices 17 and 56, both inclusive
    start_index = string.find(min(string[17:57])) + 17
    end_index = string.find(max(string[17:57])) + 18
    # Create a new string that contains only the characters between indices 17 and 56, both inclusive
    sub_string = string[start_index : end_index]
    # Find the character with the 9th smallest ASCII value among those characters in the new string
    nth_smallest_ascii = sub_string.split(' ')[8]
    return nth_smallest_ascii
