
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 46 + 1):
        substring = s[i:i+46]
        if len(set(substring)) == 46 and all(c not in substrings for c in substring):
            substrings.append(substring)
    return substrings
