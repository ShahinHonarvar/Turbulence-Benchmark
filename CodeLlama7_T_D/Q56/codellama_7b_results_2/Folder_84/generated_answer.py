
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 114 + 1):
        substring = string[i:i+114]
        if len(substring) == 114 and all(c not in substrings for c in substring)):
            substrings.append(substring)

    return substrings
