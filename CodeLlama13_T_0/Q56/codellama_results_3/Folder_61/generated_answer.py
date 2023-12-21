
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 38):
        substring = s[i:i+39]
        if len(set(substring)) == 39 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
