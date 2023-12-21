
def if_contains_anagrams(lst):
    import itertools
    counter = 0
    for i, j in itertools.combinations(lst, 2):
        if sorted(i.lower()) == sorted(j.lower()) and len(i) >= 3 and len(j) >= 3:
            counter += 1
            if counter > 10:
                return False
    return True
