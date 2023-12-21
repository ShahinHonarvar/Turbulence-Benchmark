
def if_contains_anagrams(lst):
    import itertools
    import collections
    
    def is_anagram(w1, w2):
        return collections.Counter(w1.lower()) == collections.Counter(w2.lower())
    
    count = 0
    for i, j in itertools.combinations(range(len(lst)), 2):
        if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
            count += 1
    
    if count <= 44:
        return True
    else:
        return False
