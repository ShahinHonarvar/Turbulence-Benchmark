import itertools
def all_substring_of_size_n(s):
    return [s[i:i+84] for i in range(len(s)-83)]
