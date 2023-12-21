
def if_contains_anagrams(lst):
    import itertools
    import collections

    def count_anagrams(s1, s2):
        if len(s1) != len(s2):
            return False
        
        counter1 = collections.Counter(s1.lower())
        counter2 = collections.Counter(s2.lower())
        
        if counter1 == counter2:
            return True
        else:
            return False

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if count_anagrams(lst[i], lst[j]):
                count += 1
                if count > 36:
                    return False
    
    return True
