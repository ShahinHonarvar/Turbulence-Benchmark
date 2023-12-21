import itertools
def all_substring_of_size_n(s):
    return [s[i:j] for i in range(len(s)-32) for j in range(i+32, len(s))]
