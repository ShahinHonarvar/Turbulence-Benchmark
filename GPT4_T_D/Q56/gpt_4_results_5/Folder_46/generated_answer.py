
def all_substring_of_size_n(s):
    n = 87
    substrings = list(set([s[i:i+n] for i in range(len(s)-n+1)]))
    distinct_substrings = [sub for sub in substrings if len(set(sub)) == len(sub)]
    return distinct_substrings
