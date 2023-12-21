def if_contains_anagrams(texts):
    res = False
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            s1 = texts[i]
            s2 = texts[j]
            s1 = s1.lower()
            s2 = s2.lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if s1 == s2:
                    res = True
                    break
    return res
