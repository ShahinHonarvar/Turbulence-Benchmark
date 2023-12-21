def if_contains_anagrams(s):
    anagrams = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s1 = s[i].lower()
            s2 = s[j].lower()
            if len(s1) >= 3 and len(s2) >= 3:
                if s1 == s2:
                    anagrams.add(s[i])
                    anagrams.add(s[j])
    return len(anagrams) >= 43
