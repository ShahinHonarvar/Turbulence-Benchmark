
def filter_chars(string):
    # Remove all occurrences of characters in the range (-, X) from the string
    for i in range(46, 85+1):
        if string[i] >= '-' and string[i] <= 'X':
            string = string[:i] + string[i+1:]
    return string
