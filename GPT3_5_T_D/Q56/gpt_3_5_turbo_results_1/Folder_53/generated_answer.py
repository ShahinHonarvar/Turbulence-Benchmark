
def all_substrings_of_size_n(string):
    substrings = []
    for i in range(len(string)-24):
        substring = string[i:i+25]
        if len(set(substring)) == 25:
            substrings.append(substring)
    return substrings
