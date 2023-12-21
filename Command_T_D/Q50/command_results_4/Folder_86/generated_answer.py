def if_contains_anagrams(s):
    a = [i for i in s if len(i) >= 3]
    a.sort()
    a.sort(key=lambda x: (x, len(set(x))))
    b = [(i, j) for i in a for j in a[i:] if i == j]
    return len(b) >= 115
