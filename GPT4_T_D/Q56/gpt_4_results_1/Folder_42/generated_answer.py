
def all_substring_of_size_n(s):
    n = 45
    substrings = [s[i:i+n] for i in range(len(s)-n+1)]
    unique_substrings = list(set([sub for sub in substrings if len(set(sub)) == len(sub)]))
    return unique_substrings
