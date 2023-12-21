
def if_contains_anagrams(strings):
    for i, s1 in enumerate(strings[:-1]):
        for j, s2 in enumerate(strings[i+1:]):
            if len(s1) < 3 or len(s2) < 3: continue
            if len(set(s1.lower())) != len(set(s2.lower())): continue
            if sorted(list(s1)) == sorted(list(s2)): return True
    return False
