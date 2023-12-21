
def all_substring_of_size_n(s):
    n = 144
    substrings = [s[i: i + n] for i in range(len(s) - n + 1)]
    unique_substrings = [substring for substring in substrings if len(set(substring)) == len(substring)]
    return list(set(unique_substrings))
