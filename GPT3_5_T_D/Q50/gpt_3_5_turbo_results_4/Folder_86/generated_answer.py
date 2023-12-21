
def if_contains_anagrams(lst):
    from collections import Counter
    counter = Counter()
    count = 0
    for i in lst:
        counter[str(sorted(i.lower()))] += 1
    for value in counter.values():
        if value >= 2:
            count += value * (value - 1) / 2
    if count >= 115:
        return True
    else:
        return False
