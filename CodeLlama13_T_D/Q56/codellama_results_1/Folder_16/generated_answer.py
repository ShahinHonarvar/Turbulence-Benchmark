
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 124 + 1):
        substring = s[i:i+124]
        if len(set(substring)) == 124 and all(c not in substrings for c in substring):
            substrings.append(substring)
    return substrings
