
def all_substring_of_size_n(s):
    substrings = {s[i: i+2] for i in range(len(s) - 1) if len(set(s[i: i+2])) == 2}
    return list(substrings)
