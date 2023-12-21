
def all_substring_of_size_n(s):
    n = 77
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
