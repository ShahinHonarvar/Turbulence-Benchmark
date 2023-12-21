
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 96:
        return substrings
    for i in range(len(string) - 95):
        substring = string[i:i+96]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
