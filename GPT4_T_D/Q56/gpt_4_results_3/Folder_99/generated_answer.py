
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        if len(set(s[i:i+110])) == 110:
            substrings.add(s[i:i+110])
    return list(substrings)
