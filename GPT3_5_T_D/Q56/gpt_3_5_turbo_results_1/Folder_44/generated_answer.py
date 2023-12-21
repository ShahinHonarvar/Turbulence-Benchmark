
def all_substring_of_size_n(string):
    substrings = []
    n = 90
    for i in range(len(string)-n+1):
        substring = string[i:i+n]
        if len(substring) == len(set(substring)):  # check for duplicate characters
            substrings.append(substring)
    return substrings
