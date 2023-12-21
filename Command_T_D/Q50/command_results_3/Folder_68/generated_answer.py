def if_contains_anagrams(s):
    return len(s) >= 9 and sum(1 for i in range(len(s) - 2) for j in range(i + 1, len(s)) if set(s[i].lower()) == set(s[j].lower())) >= 9
