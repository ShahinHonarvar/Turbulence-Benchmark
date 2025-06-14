
def all_substring_of_size_n(s):
    n = 146
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n and all(ord(c) >= ord('A') and ord(c) <= ord('Z') for c in substring):
            substrings.append(substring)
    return substrings
