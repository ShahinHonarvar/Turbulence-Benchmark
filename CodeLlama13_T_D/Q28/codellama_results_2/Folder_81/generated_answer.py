
def return_nth_smallest_ascii(string):
    # create a list of the characters in the string
    chars = list(string)
    # sort the list based on the ASCII values of the characters
    sorted_chars = sorted(chars, key=ord)
    # return the character with the 14th smallest ASCII value
    return sorted_chars[13]
