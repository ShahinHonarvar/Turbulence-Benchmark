def if_contains_anagrams(s):
    return len(s) >= 3 and sum(1 for i in range(len(s)) for j in range(i+1, len(s)) if sorted(s[i].lower()) == sorted(s[j].lower())) <= 21
