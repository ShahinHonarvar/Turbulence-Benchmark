
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 98 + 1):
        substring = s[i:i+98]
        if len(set(substring)) == 98 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
