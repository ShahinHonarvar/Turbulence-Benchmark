import itertools
def all_substring_of_size_n(s):
    return [s[i:j+21] for i in range(len(s)-20) for j in range(i, min(i+20, len(s)))]
