
def all_substrings_of_size_n(string):
    substrings = []
    for i in range(len(string) - 95):
        substring = string[i:i+96]
        if len(set(substring)) == 96:
            substrings.append(substring)
    return substrings
