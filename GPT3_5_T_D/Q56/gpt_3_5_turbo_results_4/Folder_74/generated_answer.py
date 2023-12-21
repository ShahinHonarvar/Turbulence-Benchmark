
def all_substring_of_size_n(string):
    n = 97
    substrings = []
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        if len(substr) == len(set(substr)):
            substrings.append(substr)
    return list(set(substrings))
