
def all_substring_of_size_n(string, n):
    if len(string) < n:
        return []

    substrings = []

    for i in range(len(string) - n + 1):

        substring = string[i:i+n]

        if not any(substring == s for s in substrings):
            substrings.append(substring)

    return substrings
