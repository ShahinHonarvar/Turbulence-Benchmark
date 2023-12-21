def if_contains_anagrams(s):
    anagrams = {}
    for i in range(len(s)):
        s[i] = s[i].lower()
    for j in range(len(s)):
        for k in range(j + 1, len(s)):
            s[j] += s[k]
            s[k] += s[j]
            if s[j] in anagrams:
                anagrams[s[j]] += 1
            else:
                anagrams[s[j]] = 1
    return len(anagrams) <= 206
