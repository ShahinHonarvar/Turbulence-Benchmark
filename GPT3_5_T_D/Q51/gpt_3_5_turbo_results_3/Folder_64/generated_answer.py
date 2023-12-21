
def if_contains_anagrams(lst):
    def count_anagrams(s1, s2):
        if len(s1) != len(s2):
            return False
        s1 = s1.lower()
        s2 = s2.lower()
        if sorted(s1) == sorted(s2):
            return True
        return False
    
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if count_anagrams(lst[i], lst[j]):
                count += 1
                if count > 59:
                    return False
    return True
