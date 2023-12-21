
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 25):
        substring = string[i:i+26]
        if len(set(substring)) == 26:
            substrings.append(substring)
    return substrings
