
def if_contains_anagrams(lst):
    import itertools
    counter = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if (sorted(list(lst[i].lower())) == sorted(list(lst[j].lower()))) and (len(lst[i]) >= 3):
                counter += 1
                if counter > 86:
                    return False
    return True
