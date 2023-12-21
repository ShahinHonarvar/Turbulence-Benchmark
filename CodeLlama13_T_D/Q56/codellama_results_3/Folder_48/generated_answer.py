
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 120 + 1):
        substring = s[i:i+120]
        if len(set(substring)) == 120 and all(c.isalpha() for c in substring):
            substrings.append(substring)
    return substrings
