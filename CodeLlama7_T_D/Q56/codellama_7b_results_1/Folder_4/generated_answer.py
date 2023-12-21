
def all_substring_of_size_n(string, n):
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) == n and substring not in substrings:
            substrings.append(substring)

    return substrings
