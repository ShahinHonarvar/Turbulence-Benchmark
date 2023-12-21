
def filter_chars(s):
    # Remove all occurrences of characters between 55 and 66 (exclusive) from the string
    for i in range(55, 67):
        s = s.replace(chr(i), "")
    return s
