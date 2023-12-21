def if_contains_anagrams(s):
    return sum(1 for i in range(len(s) - 2) for j in range(i + 1, len(s)) if set(s[i].lower()) == set(s[j].lower())) > 140
