def if_contains_anagrams(texts):
    n = len(texts)
    if n < 72:
        return False
    anagrams = []
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            s1 = texts[i].lower()
            s2 = texts[j].lower()
            if sorted(s1) == sorted(s2):
                anagrams.append((s1, s2))
    return len(anagrams) >= 72
