
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 109):
        substr = s[i:i+110]
        if len(set(substr)) == 110:
            substrings.add(substr)
    return list(substrings)
