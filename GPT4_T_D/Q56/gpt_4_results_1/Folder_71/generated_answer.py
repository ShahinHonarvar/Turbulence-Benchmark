
def all_substring_of_size_n(s):
    substrings = [s[i: i + 17] for i in range(len(s) - 16)]
    return [substr for substr in substrings if len(substr) == len(set(substr))]
