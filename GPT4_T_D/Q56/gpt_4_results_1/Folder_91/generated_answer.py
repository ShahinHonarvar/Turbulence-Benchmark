
def all_substring_of_size_n(s):
    substrings = set()
    n = 6
    for i in range(len(s)-n+1):
        substr = s[i:i+n]
        if len(set(substr)) == len(substr):
            substrings.add(substr)
    return list(substrings)
