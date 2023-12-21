
def all_substring_of_size_n(s):
    n = 68
    substrings = {s[i: i+n] for i in range(len(s) - n + 1)}

    return list(filter(lambda sub: len(set(sub)) == len(sub), substrings))
