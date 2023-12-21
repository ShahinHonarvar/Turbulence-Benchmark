
def remove_repeat_chars(s):
    # Find the indices of the characters that occur more than once
    indices = []
    for i in range(44, 78):
        if s[i] not in indices:
            indices.append(i)
    # Remove all occurrences of each character at its indices
    for i in reversed(indices):
        s = s[:i] + s[i+1:]
    return s
