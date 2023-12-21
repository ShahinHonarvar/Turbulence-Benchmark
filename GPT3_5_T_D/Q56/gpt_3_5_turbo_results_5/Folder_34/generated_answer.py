
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 83):
        substr = string[i:i+84]
        if len(set(substr)) == 84:
            substrings.append(substr)
    return substrings
