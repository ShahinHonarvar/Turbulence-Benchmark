
def all_substring_of_size_n(s):
    n = 65
    substrings = []
    for i in range(len(s) - n + 1):
        substr = s[i:i+n]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return list(set(substrings))
