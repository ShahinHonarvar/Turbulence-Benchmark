
def all_substring_of_size_n(string):
    substrings = set()
    n = len(string)
    if n < 36:
        return []
    for i in range(n - 35):
        substring = string[i:i + 36]
        if len(set(substring)) == 36:
            substrings.add(substring)
    return list(substrings)
