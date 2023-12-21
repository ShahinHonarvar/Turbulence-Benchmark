
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 25):
        substr = string[i:i+26]
        if len(set(substr)) == 26:
            if substr not in substrings:
                substrings.append(substr)
    return substrings
