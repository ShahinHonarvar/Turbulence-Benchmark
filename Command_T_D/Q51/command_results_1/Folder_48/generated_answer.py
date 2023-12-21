def if_contains_anagrams(texts):
    letters = set(str('abcdefghijklmnopqrstuvwxyz'))
    return sum(1 for s1, s2 in zip(texts, texts[1:]) if s1 == s2[::-1] and len(s1) >= 3 and all(c in letters for c in s1)) <= 277
