
def remove_repeat_chars(s):
    # Find the indices of the characters that occur more than once between the given indices
    indices = []
    for i in range(36, 54):
        if s[i] in indices:
            continue

        else:

            indices.append(i)

    # Remove all occurrences of each character from the string
    for i in reversed(indices):
        s = s[:i] + s[i+1:]
    return s
