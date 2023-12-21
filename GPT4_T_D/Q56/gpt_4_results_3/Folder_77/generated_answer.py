
def all_substring_of_size_n(s):
    substrings = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(set(s[i: j]))==144 and len(s[i: j])==144]
    distinct_substrings=list(set(substrings))
    return distinct_substrings
