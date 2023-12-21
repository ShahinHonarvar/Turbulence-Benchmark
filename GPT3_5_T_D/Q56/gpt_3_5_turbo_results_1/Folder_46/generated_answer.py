
def all_substrings_of_size_n(string):
    substrings = []
    for i in range(len(string) - 86):
        substring = string[i:i+87]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
