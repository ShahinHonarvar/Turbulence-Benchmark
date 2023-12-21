
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string) - 116):
        substr = string[i:i+117]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return substrings
