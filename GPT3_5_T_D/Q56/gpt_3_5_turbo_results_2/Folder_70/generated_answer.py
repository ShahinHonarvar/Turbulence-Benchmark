
def all_substring_of_size_n(string):
    substrings = []
    if len(string) < 12:
        return substrings
    for i in range(len(string) - 11):
        substring = string[i:i+12]
        if len(set(substring)) == 12:
            substrings.append(substring)
    return substrings
