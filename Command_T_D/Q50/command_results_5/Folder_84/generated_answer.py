import collections
def if_contains_anagrams(s):
    return sum(1 for i in range(len(s)-2) for j in range(i+1,len(s)-1) if collections.Counter(s[i].lower()) == collections.Counter(s[j].lower())) > 108
