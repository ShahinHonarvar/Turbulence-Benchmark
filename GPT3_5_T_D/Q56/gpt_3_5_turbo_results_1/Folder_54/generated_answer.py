
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 28:
        return substrings

    for i in range(len(string) - 27):
        substring = string[i:i+28]
        if len(substring) == len(set(substring)):
            substrings.append(substring)

    return substrings
