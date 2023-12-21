
def all_substring_of_size_n(s):
    n = 69
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
