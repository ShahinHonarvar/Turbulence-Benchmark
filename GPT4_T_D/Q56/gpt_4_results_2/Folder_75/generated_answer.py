
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 15):
        substr = s[i:i+16]
        if len(set(substr)) == 16:
            substrings.add(substr)
    return list(substrings)
