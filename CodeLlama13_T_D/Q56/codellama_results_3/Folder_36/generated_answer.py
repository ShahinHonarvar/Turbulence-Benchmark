
def all_substring_of_size_n(s, n):
    substrings = []
    for i in range(len(s) - n + 1):
        substring = s[i:i+n]
        if not any(substring in s[:i] or substring in s[i+n:] for j in range(len(s))):
            substrings.append(substring)
    return substrings
