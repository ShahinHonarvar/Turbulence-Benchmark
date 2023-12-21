
def all_substring_of_size_n(s):
    substrings = list(set([s[i: i + 2] for i in range(len(s) - 1)]))
    return [substring for substring in substrings if len(set(substring)) == 2]
