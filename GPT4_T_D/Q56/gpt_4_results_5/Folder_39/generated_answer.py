
def all_substring_of_size_n(s):
    n = 94
    substrings = [s[i:i+n] for i in range(len(s) - n + 1)]
    return list(set(filter(lambda x: len(set(x)) == len(x), substrings)))
