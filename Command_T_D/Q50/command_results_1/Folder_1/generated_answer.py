def if_contains_anagrams(s):
    return len(s) >= 96 and any(set(s[i]).intersection(s[j]) == set(s[i]) for i in range(len(s)) for j in range(i + 1, len(s)))
