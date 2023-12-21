
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-7):
        substring = string[i:i+8]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return list(set(substrings))
