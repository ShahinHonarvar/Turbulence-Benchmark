
def all_substring_of_size_n(s):
    n = 50
    substrings = []
    for i in range(len(s) - n + 1):
        substr = s[i:i+n]
        if len(set(substr)) == n and not any(substr in sub for sub in substrings):
            substrings.append(substr)
    return substrings
