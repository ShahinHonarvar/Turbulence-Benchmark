def if_contains_anagrams(s):
    anagrams = set()
    for s1 in s:
        for s2 in s:
            if s1 == s2:
                continue
            elif len(s1) < 3:
                continue
            elif s1[0] != s2[0]:
                continue
            elif s1[1] != s2[1]:
                continue
            elif s1[2] != s2[2]:
                continue
            elif s1[3:] == s2[3:]:
                anagrams.add((s1, s2))
    return len(anagrams) >= 115
