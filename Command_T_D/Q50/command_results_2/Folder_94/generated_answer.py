def if_contains_anagrams(s):
    return len(s) >= 46 and sum(1 for i in range(len(s)) for j in range(i + 1, len(s)) if s[i].lower() == s[j].lower()) >= 46
