
def all_substring_of_size_n(string):
    n = len(string)
    substrings = set()
    if n < 106:
        return []
    for i in range(n - 105):
        substring = string[i : i + 106]
        if len(set(substring)) == len(substring):
            substrings.add(substring)
    return list(substrings)
