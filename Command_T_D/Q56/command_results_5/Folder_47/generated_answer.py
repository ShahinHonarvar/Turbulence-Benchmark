import itertools
def all_substring_of_size_n(s):
    return [s[i:j+1] for i in range(len(s)-90) for j in range(i+1, len(s)+1)]
