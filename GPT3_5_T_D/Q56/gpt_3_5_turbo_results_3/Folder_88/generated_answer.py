
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 67):
        if len(set(string[i:i+68])) == 68:
            substrings.append(string[i:i+68])
    return substrings
