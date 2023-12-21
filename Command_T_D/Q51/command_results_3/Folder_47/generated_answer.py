def if_contains_anagrams(s):
    return all(s[i] == s[j] for i, s[i] in enumerate(s) for j in range(i + 1, len(s)))
