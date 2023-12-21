
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 26 + 1):
        substring = string[i: i + 26]
        if len(set(substring)) == 26:
            substrings.add(substring)
    return list(substrings)
