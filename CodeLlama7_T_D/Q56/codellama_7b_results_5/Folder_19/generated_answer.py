
def all_substring_of_size_n(s):
    n = len(s)
    substrings = []
    for i in range(n - 18 + 1):
        substring = s[i:i+18]
        if not any(c in substrings for c in substring):
            substrings.append(substring)

    return substrings
