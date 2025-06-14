
def all_substring_of_size_n(string, n):
    if len(string) < n:
        return []

    substrings = []

    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if all([c not in substrings for c in substring]):
            substrings.append(substring)

    return substrings
