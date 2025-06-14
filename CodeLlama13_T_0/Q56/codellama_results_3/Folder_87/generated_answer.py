
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 58 + 1):
        substring = s[i:i+58]
        if len(set(substring)) == 58 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
