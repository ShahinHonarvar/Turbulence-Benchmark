
def all_substring_of_size_n(string):
    n = 105
    substrings = set()
    if len(string) < n:
        return []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
