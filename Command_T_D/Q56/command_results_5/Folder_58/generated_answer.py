import itertools
def all_substring_of_size_n(s):
    return [s[i:j+127] for i in range(0, len(s)-127) for j in range(i, min(len(s)-1, i+127))]
