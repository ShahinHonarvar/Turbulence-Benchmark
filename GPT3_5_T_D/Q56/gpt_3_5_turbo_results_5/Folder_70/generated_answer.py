
def all_substring_of_size_n(string):
    substrings = []
    n = 12
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return list(set(substrings))
