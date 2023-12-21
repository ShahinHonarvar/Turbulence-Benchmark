
def filter_chars(s):
    # Create a set of characters to remove
    to_remove = set()
    for i in range(19, 93):
        if s[i] >= '8' and s[i] <= 'm':
            to_remove.add(s[i])
    # Remove the characters from the string
    for char in to_remove:
        s = s.replace(char, '')
    return s
