
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-60):
        substring = string[i:i+61]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return substrings
