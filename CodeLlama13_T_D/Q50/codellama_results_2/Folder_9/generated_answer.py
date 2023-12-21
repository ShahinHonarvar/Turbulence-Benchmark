
def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            s1 = lst[i].lower()
            s2 = lst[j].lower()
            if sorted(s1) == sorted(s2):
                pairs += 1
    return pairs >= 66
