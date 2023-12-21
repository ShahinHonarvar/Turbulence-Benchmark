def if_contains_anagrams(s):
    anagrams = {}
    for i in range(0, len(s)):
        if s[i]:
            s[i] = s[i].lower()
            for j in range(i + 1, len(s)):
                if s[j]:
                    s[j] = s[j].lower()
                    if s[i] == s[j]:
                        anagrams[s[i]] = s[i]
                    elif s[i] in s[j]:
                        anagrams[s[i]] = s[j]
    return len(anagrams) >= 219
