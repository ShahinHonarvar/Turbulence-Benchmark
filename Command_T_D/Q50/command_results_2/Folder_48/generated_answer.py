def if_contains_anagrams(s):
    return sum(1 for i in range(len(s)) for j in range(i+1, len(s)) if all(c1 == c2 for c1, c2 in zip(s[i].lower(), s[j].lower()))) >= 219
