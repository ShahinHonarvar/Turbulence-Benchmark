
def all_substring_of_size_n(string):
    substrings = []
    for i in range(len(string)-32):
        substr = string[i:i+33]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return list(set(substrings))
