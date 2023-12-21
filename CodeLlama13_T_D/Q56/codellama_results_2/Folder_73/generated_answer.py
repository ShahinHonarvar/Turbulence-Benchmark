
def all_substring_of_size_n(s, n):
    substrings = []
    for i in range(len(s)):
        substring = s[i:i+n]
        if len(substring) == n and not any(c in substrings for c in substring):
            substrings.append(substring)
    return substrings
