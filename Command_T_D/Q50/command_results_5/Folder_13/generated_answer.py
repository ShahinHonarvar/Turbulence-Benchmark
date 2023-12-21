import collections
def if_contains_anagrams(s):
    return len(list( filter(lambda s1,s2: s1==s2 or s1.lower()==s2.lower(),s) ) )>=144
