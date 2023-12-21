
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 14):
        substr = s[i:i+15]
        if len(set(substr)) == 15 and not any(c in substrings for c in substr):
            substrings.append(substr)
    return substrings
