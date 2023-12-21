
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 28):
        substring = string[i:i+29]
        if len(set(substring)) == 29:
            substrings.append(substring)
    return substrings
