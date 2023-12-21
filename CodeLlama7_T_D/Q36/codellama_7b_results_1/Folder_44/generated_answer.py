
def filter_chars(string):
    # Remove all occurrences of characters between indices 18 and 64 (both exclusive)
    for i in range(18, len(string)):
        if string[i] > '3' and string[i] < 'B':
            string = string[:i] + string[i+1:]
    return string
