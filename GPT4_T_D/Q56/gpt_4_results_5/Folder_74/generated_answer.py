
def all_substring_of_size_n(s):

    n = 97

    substrings = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) == n]

    distinct_substrings = [sub for sub in substrings if len(set(sub)) == n]

    return list(set(distinct_substrings))
