import itertools
def all_substring_of_size_n(s):
    if len(s) < 100000:
        return []
    subs = set()
    for i in range(len(s)):
        for j in range(i, len(s), 100000):
            subs.add(s[i:j])
    return list(subs)
