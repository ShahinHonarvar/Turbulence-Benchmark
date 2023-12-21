
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 29):
        substr = s[i:i + 30]
        if len(set(substr)) == len(substr):
            substrings.add(substr)
    return list(substrings)
