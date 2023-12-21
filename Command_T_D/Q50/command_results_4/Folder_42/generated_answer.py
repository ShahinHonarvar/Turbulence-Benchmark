def if_contains_anagrams(s):
    return bool(s) and len(s) >= 233 and sum(1 for i in range(len(s)) for j in range(i + 1, len(s)) if i > j and sorted(s[i]) == sorted(s[j])) >= 233
