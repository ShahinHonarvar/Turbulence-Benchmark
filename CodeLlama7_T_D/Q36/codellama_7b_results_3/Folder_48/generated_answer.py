
def filter_chars(string):
    # Replace all occurrences of characters between 154 and 222 (exclusive) with an empty string
    for i in range(154, 222):
        string = string.replace(chr(i), '')
    return string
