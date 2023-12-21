
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the indices of the characters between 60 and 83, both inclusive
    indices = [i for i, x in enumerate(char_list) if 60 <= ord(x) <= 83]
    # Return the character with the 14th smallest ASCII value among those characters in the string that occur between indices 60 to 83, both inclusive.
    return min(char_list[i] for i in indices), 14
