import re
def return_n_smallest_chars(s):
    char_set = set(s)
    if len(char_set) > 52:
        char_set = char_set[:52]
    return sorted(char_set)[::-1]
