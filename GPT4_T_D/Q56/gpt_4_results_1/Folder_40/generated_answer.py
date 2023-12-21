
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)-1):
        substr = s[i:i+2]
        if len(set(substr)) == 2:
            substrings.add(substr)
    return list(substrings)
