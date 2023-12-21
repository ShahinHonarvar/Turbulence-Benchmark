
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 89:
        return substrings
    for i in range(len(string)-88):
        substring = string[i:i+89]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return list(set(substrings))
