import itertools
def all_substring_of_size_n(s):
    return [s[i:j] for i in range(len(s)-47) for j in range(i+48)]
