
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 40):
        substring = s[i:i+41]
        if len(set(substring)) == 41 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
