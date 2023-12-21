
import itertools

def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s)-40):
        substr = s[i:i+41]
        if len(set(substr)) == len(substr):
            substrings.append(substr)
    return substrings
