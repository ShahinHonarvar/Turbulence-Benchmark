
def all_substring_of_size_n(s):
    n = 29
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if len(set(substring)) == n and not any(substring in s[:i] or substring in s[i+n:]):
            substrings.append(substring)
    return substrings
