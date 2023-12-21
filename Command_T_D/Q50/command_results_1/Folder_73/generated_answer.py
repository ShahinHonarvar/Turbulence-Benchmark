def if_contains_anagrams(s):
    res = False
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if(s[i].lower() == s[j].lower()):
                if(s[i] != s[j]):
                    res = True
                    break
    return res
