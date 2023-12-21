
def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 23:
        return substrings
    else:
        for i in range(len(s) - 22):
            substr = s[i:i+23]
            if len(set(substr)) == 23:
                substrings.append(substr)
    return list(set(substrings))
