
def if_contains_anagrams(lst):
    from itertools import combinations
    count = 0
    for i, j in combinations(lst, 2):
        if len(i) >= 3 and len(j) >= 3 and sorted(i.lower()) == sorted(j.lower()):
            count += 1
            if count > 64:
                return False
    return True
