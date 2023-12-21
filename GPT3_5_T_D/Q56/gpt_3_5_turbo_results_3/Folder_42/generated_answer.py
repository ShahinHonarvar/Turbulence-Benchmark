
def all_substrings_of_size_n(string):
    if len(string) < 45:
        return []
    substrings = []
    for i in range(len(string) - 44):
        substring = string[i:i+45]
        if len(set(substring)) == 45:
            substrings.append(substring)
    return substrings
