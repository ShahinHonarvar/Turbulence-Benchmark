
def if_contains_anagrams(lst):
    import collections
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if collections.Counter(lst[i].lower()) == collections.Counter(lst[j].lower()):
                    count += 1
            if count > 423:
                return False
    return True
