
def all_substring_of_size_n(string):
    substrings = set()
    n = len(string)
    for i in range(n - 148):
        for j in range(i, i + 149):
            substring = string[i:j + 1]
            if len(substring) == 149 and len(set(substring)) == 149:
                substrings.add(substring)
    return list(substrings)
