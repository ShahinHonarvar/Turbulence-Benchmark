
def all_substring_of_size_n(s):
    if len(s) < 53:
        return []
    substrings = set()
    for i in range(len(s)-52):
        substr = s[i:i+53]
        if len(set(substr)) == 53:
            substrings.add(substr)
    return list(substrings)
