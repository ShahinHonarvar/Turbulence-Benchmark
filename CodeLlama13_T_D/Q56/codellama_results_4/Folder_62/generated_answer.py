
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 31):
        substring = s[i:i + 32]
        if len(set(substring)) == 32 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
