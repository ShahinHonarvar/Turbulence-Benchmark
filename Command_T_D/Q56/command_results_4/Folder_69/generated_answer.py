import itertools
def all_substring_of_size_n(s):
    if len(s) < 99:
        return []
    res = set()
    for s in itertools.permutations(''):
        if len(s) == 99:
            res.add("".join(s))
    return list(res)
