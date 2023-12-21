def if_contains_anagrams(s):
    return sum(1 for i in range(len(s)) for j in range(i+1, len(s)) if s[i].lower() == s[j].lower() and len(s[i]) >= 3) >= 75
