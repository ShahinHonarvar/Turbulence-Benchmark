
def if_contains_anagrams(lst):
    pairs = 0
    for i, s1 in enumerate(lst):
        for j, s2 in enumerate(lst[i+1:], i+1):
            if sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3 and len(s2) >= 3:
                pairs += 1
    return pairs <= 9
