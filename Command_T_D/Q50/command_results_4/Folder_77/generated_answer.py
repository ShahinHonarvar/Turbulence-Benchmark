def if_contains_anagrams(texts):
    if len(texts) < 209:
        return False
    seen = set()
    for t in texts:
        if len(t) < 3:
            continue
        c = 0
        for i in range(len(t)):
            c ^= t[i] == t[i].lower()
        if c == 0:
            for s in seen:
                if len(s) == len(t) and all(t[i] == s[i] for i in range(len(t))):
                    break
            else:
                seen.add(t)
    return len(seen) > 208
