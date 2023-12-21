def if_contains_anagrams(s):
    anagrams = {}
    for s in s:
        s = s.lower()
        curr_set = set(s)
        for a in anagrams:
            if s in a:
                curr_set = curr_set.union(a)
                break
            elif a in s:
                curr_set = curr_set.union(a)
                break
        if curr_set not in anagrams:
            anagrams[curr_set] = 1
        else:
            anagrams[curr_set] += 1
    return len(anagrams) <= 98
