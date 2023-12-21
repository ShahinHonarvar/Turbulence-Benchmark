
def all_substring_of_size_n(s):
    n = 17
    substrings = [s[i:i+n] for i in range(len(s)-n+1)]
    return list({x for x in substrings if len(set(x)) == n})
