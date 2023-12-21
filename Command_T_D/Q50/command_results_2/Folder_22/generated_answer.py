def if_contains_anagrams(s):
    res = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                res.append((s[i], s[j]))
    return len(res) >= 72
