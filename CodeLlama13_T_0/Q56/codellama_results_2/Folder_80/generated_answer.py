
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 30):
        substring = s[i:i+31]
        if len(set(substring)) == 31 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
