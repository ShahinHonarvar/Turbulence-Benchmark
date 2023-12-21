
def all_substring_of_size_n(s):
    substrings = []
    n = 64
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return substrings
