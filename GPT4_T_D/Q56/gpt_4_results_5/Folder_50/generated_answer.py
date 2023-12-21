
def all_substring_of_size_n(s):
    if len(s) < 11:
        return []
    substrings = []
    for i in range(len(s) - 10):
        substr = s[i:i+11]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return list(set(substrings))
