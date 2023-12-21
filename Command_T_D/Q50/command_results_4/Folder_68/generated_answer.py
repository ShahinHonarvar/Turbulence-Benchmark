def if_contains_anagrams(s):
    return sum(
        1
        for i in range(len(s))
        for j in range(i + 1, len(s))
        if s[i] == s[j]
        and len(s[i]) >= 3
        and (s[i] * len(s[i]) == s[j] * len(s[j]) or s[i] == s[j])
    ) >= 9
