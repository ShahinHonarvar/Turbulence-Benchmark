
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(set(substring)) == n and not any(c in substring for c in substrings):
            substrings.append(substring)
    return substrings
