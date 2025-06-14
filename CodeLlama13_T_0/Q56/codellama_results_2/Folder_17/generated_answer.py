
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 36):
        substring = s[i:i+37]
        if len(set(substring)) == 37 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
