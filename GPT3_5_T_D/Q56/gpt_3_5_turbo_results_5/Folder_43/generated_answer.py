
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 86:
        return substrings

    for i in range(len(string) - 85):
        substring = string[i:i+86]
        if len(set(substring)) == 86:
            substrings.append(substring)

    return substrings
