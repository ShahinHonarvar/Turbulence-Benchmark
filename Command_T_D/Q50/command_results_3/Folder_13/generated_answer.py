def if_contains_anagrams(s):
    anagrams = set()
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                continue
            elif len(s[i]) >= 3 and len(s[j]) >= 3:
                if sorted(s[i]) == sorted(s[j]):
                    anagrams.add(s[i])
                    anagrams.add(s[j])
    return len(anagrams) >= 144
