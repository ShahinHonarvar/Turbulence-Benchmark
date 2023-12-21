
def if_contains_anagrams(lst):
    from collections import Counter
    cnt = Counter()
    res = 0
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            cnt[''.join(sorted(word))] += 1
    for key in cnt:
        res += cnt[key]*(cnt[key]-1)//2
    return res <= 48
