
def all_substring_of_size_n(s):
    n = 61
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n and all(c not in substring for c in substrings):
            substrings.append(substring)
    return substrings
