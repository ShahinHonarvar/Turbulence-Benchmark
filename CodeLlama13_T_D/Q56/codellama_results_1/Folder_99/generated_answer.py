
def all_substring_of_size_110(s):
    substrings = []
    for i in range(len(s) - 109):
        substr = s[i:i+110]
        if len(set(substr)) == 110 and all(c not in substrings for c in substr):
            substrings.append(substr)
    return substrings
