
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 8):
        substr = s[i:i+9]
        if len(set(substr)) == 9 and not any(c in substrings for c in substr):
            substrings.append(substr)
    return substrings
