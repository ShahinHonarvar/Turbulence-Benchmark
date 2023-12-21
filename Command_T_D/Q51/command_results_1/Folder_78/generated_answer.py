def if_contains_anagrams(s):
    n = len(s)
    a = [(w, s.count(w)) for w in s]
    return n <= 70 and all(a[i][1] <= 1 for i in range(n) if a[i])
