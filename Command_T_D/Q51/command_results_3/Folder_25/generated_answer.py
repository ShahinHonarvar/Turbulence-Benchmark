def if_contains_anagrams(s):
    anagrams = {}
    for w in s:
        w = w.lower()
        n = len(w)
        for j in range(n):
            w_ = w[:j] + w[j+1:]
            if w_ in anagrams and w in anagrams[w_]:
                return True
            if w_ not in anagrams:
                anagrams[w_] = set()
            anagrams[w_].add(w)
    return len(anagrams) <= 67
