def if_contains_anagrams(s):
    anagrams = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                anagrams.add(s[i])
                if len(anagrams) > 15:
                    return False
    return True
