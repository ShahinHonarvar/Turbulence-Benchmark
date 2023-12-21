
def all_substring_of_size_n(s):
    n = 78
    substrings = {s[i: i+n] for i in range(len(s)-n+1) if len(set(s[i: i+n])) == n}
    return list(substrings)
