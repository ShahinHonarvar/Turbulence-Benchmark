
def all_substrings_of_size_n(string):
    substrings = []
    for i in range(len(string)-99):
        substring = string[i:i+100]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
