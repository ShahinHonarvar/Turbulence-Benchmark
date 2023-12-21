import itertools
def all_substring_of_size_n(s):
    return [s[i:j] for i in range(0, len(s)-95) for j in range(i+96, len(s))] + \
           [s[i:j] for i in range(len(s)-95, -1, -1) for j in range(i+96, i-1)] + \
           [s[i:j] for i in range(0, len(s)-95) for j in range(i+96, i)]
