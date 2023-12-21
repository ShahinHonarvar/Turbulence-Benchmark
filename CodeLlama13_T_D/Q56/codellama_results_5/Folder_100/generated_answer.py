
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 92 + 1):
        substring = s[i:i+92]
        if len(set(substring)) == 92 and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
