def if_contains_anagrams(s):
    n = len(s)
    anagrams = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i].lower() == s[j].lower():
                anagrams += 1
                break
    return anagrams > 90
