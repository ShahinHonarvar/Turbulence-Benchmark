
def all_substrings_of_size_n(string):
    substrings = []
    for i in range(len(string)):
        substring = string[i:i+11]
        if len(substring) == 11 and len(set(substring)) == 11:
            substrings.append(substring)
    return list(set(substrings))
