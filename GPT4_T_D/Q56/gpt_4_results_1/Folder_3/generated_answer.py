
def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 93 + 1):
        substr = s[i:i+93]
        if len(substr) == len(set(substr)):
            substrings.add(substr)
    return list(substrings)
