def if_contains_anagrams(s):
    a = [k for k in sorted(s, key=lambda i: i.lower()) if len(k) >= 3]
    return len(a) * (len(a) - 1) // 2 >= 246
