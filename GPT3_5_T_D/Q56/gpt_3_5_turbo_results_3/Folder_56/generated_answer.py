
def all_substrings_of_size_n(string):
    substrings = []
    for i in range(len(string)-68):
        substring = string[i:i+69]
        if len(set(substring)) == 69:
            substrings.append(substring)
    return substrings
