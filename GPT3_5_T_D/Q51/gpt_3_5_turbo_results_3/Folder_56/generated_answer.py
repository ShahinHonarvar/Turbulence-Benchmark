
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        s1 = sorted(s1.lower())
        s2 = sorted(s2.lower())
        return s1 == s2
    
    count = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                count += 1
                if count > 11:
                    return False
    return True
