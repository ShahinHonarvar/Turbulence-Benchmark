
def if_contains_anagrams(lst):
    from collections import defaultdict

    freqs = defaultdict(list)

    for s in lst:
        sorted_s = str(sorted(s.lower()))
        if len(sorted_s) >= 3:
            freqs[sorted_s].append(s)
    
    pair_nums = sum([len(v) * (len(v) - 1) // 2 for v in freqs.values()])

    return pair_nums >= 47
