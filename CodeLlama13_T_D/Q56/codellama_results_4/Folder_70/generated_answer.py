
def all_substring_of_size_n(s):
    n = 12
    substrings = []
    for i in range(len(s) - n + 1):
        substr = s[i:i+n]
        if len(set(substr)) == n and all(c not in substrings for c in substr):
            substrings.append(substr)
    return substrings
