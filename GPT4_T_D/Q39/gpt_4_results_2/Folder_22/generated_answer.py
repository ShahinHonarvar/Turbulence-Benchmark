
def return_n_greatest_chars(s):
    # Sort the characters in the string in descending order and take the first 76
    greatest_chars = sorted(s, reverse=True)[:76]
    # sort the list in ascending order
    greatest_chars.sort()
    return greatest_chars
