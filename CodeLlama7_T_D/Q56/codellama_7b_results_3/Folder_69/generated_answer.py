
def all_substring_of_size_n(s):
    n = len(s) - 1
    substrings = []
    for i in range(0, n + 1):
        substring = s[i:i + 99]
        if not any(c in substrings for c in substring):
            substrings.append(substring)

    return substrings
