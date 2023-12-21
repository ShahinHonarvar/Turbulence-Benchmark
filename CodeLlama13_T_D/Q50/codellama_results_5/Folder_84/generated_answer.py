
def if_contains_anagrams(lst):
    for i, s in enumerate(lst):
        for j in range(i+1, len(lst)):
            t = lst[j]
            if len(s) < 3 or len(t) < 3: continue
            if sorted(s.lower()) == sorted(t.lower()): return True
    return False
