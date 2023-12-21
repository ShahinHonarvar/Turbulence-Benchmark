
def all_substring_of_size_n(string):
    substrings = []
    length = len(string)
    if length < 52:
        return substrings
    for i in range(length - 51):
        substring = string[i:i+52]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
