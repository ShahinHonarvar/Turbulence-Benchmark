
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 83):
        substr = s[i:i + 84]
        if len(set(substr)) == 84 and not any(c in substrings for c in substr):
            substrings.append(substr)
    return substrings
