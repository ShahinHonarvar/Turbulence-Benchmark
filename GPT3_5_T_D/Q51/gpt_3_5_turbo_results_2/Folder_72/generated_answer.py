
def if_contains_anagrams(strings):
    import itertools
    counter = 0
    for s1, s2 in itertools.combinations(strings, 2):
        if len(s1) >= 3 and s1.lower() == s2.lower() and sorted(s1.lower()) == sorted(s2.lower()):
            counter += 1
            if counter > 188:
                return False
    return True
