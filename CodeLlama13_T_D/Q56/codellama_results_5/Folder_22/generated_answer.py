
def all_substring_of_size_n(s):
    n = 22
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n and not any(c*2 in substring for c in substring):
            substrings.append(substring)
    return substrings
