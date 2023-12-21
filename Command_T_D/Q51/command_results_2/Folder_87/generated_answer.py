import collections
def if_contains_anagrams(test_list):
    res = collections.Counter(test_list)
    for x in res:
        if res[x] > 1:
            res[x] -= 1
            res[''.join(sorted(x.lower()))] += 1
    return all(v == 1 for v in res.values())
