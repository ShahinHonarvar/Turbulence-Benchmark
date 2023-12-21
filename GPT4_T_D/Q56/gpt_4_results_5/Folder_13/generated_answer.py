
def all_substring_of_size_n(string):
    substrings = set()
    for i in range(len(string) - 52):
        substring = string[i: i + 53]
        if len(substring) == len(set(substring)):
            substrings.add(substring)
    return list(substrings)
