def if_contains_anagrams(s):
    return sum(1 for i in range(len(s)) for j in range(i+1, len(s)) if anagrams(s[i], s[j])) >= 91
def anagrams(a, b):
    return sorted(set(a.lower())) == sorted(set(b.lower()))
