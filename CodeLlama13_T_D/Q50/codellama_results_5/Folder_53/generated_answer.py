
def if_contains_anagrams(lst):
    for i, s in enumerate(lst):
        for j in range(i+1, len(lst)):
            if s != lst[j] and sorted(s.lower()) == sorted(lst[j].lower()):
                return True
    return False
