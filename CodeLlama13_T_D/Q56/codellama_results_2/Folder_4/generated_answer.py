
def all_substring_of_size_n(s):
    n = 41
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)-n+1):
            substring = s[i:j]
            if len(substring) == n and all(c not in substring for c in substring[:-1]):
                substrings.append(substring)
    return substrings
