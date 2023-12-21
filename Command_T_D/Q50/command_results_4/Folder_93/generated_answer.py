def if_contains_anagrams(s):
    res = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                continue
            elif len(s[i]) >= 3 and len(s[j]) >= 3:
                res += 1
    return res >= 18
