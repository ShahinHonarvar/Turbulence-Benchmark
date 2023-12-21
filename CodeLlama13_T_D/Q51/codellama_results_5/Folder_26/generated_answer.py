
def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        s1 = lst[i].lower()
        if len(s1) < 3: continue
        for j in range(i+1, len(lst)):
            s2 = lst[j].lower()
            if len(s2) < 3: continue
            if sorted(s1) == sorted(s2):
                count += 1
                if count > 35: return False
    return True
