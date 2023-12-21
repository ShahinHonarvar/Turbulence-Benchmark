
def remove_repeat_chars(s):
    # Find the indices where the character occurs more than once
    indices = []
    for i in range(34, 69):
        if s[i] in s[:i] or s[i] in s[i+1:]:
            indices.append(i)
    # Remove all occurrences of the character from the string
    for i in reversed(indices):
        s = s[:i] + s[i+1:]
    return s
