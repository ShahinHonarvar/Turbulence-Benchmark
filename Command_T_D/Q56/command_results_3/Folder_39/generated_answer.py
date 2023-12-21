import itertools
def all_substring_of_size_n(s):
    return [s[i:j+94] for i in range(0, len(s)-94+1) for j in range(i, i+94)]
