
def all_substring_of_size_n(s):
    n = 71
    substrings = []
    for i in range(len(s) - n + 1):
        substr = s[i:i+n]
        if len(set(substr)) == n and substr not in substrings:
            substrings.append(substr)
    return substrings
