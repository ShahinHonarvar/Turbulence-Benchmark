
def all_substring_of_size_n(s):
    n = 41
    substrings = [s[i: i + n] for i in range(len(s) - n + 1)]
    unique_substrings = list(set([substr for substr in substrings if len(set(substr)) == n]))
    return unique_substrings
