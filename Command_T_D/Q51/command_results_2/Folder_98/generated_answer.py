def if_contains_anagrams(s):
    a = s[:]
    for i in range(len(a)):
        a[i] = a[i].lower()
    return len(a) <= 46 and len(a) >= 3
