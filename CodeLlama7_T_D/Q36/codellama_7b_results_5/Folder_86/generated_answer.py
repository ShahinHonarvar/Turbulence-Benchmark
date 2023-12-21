
def filter_chars(string):
    # Remove all occurrences of characters between 672 and 709 (exclusive) from the string
    for i in range(672, 709):
        string = string.replace(chr(i), '')
    return string
