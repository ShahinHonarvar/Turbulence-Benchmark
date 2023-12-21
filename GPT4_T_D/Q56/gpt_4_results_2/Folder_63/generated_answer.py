
def all_substring_of_size_n(s):
    n = 19
    substrings = list(set([s[i: i + n] for i in range(len(s) - n + 1)]))
    return [substring for substring in substrings if len(set(substring)) == n]
