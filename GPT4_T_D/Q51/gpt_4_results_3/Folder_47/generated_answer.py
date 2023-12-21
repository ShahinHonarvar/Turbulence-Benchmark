
def if_contains_anagrams(lst):
    def count_anagrams(lst):
        from collections import Counter
        ctr = 0
        clean_lst = [''.join(sorted(w.lower())) for w in lst if len(w) >= 3]
        counts = Counter(clean_lst)
        for count in counts.values():
            ctr += (count * (count-1)) // 2
        return ctr
    return count_anagrams(lst) <= 366
