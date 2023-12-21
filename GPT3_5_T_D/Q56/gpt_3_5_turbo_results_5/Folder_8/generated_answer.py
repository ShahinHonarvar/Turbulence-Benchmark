
def all_substrings_of_size_n(string):
    substrings = []
    length = len(string)
    if length < 30:
        return substrings
    for i in range(length - 29):
        substring = string[i:i+30]
        if len(set(substring)) == 30:
            substrings.append(substring)
    return substrings
