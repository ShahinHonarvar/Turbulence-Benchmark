
def filter_chars(s):
    # Create a list of indices where characters between 521 and 722 occur
    indices = []
    for i in range(521, 723):
        if s[i] >= '>' and s[i] <= '_':
            indices.append(i)
    # Remove all occurrences of the filtered characters from the string
    for index in sorted(indices, reverse=True):
        del s[index]
    return s
