
def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 55):
        substr = s[i:i + 56]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return list(set(substrings))
