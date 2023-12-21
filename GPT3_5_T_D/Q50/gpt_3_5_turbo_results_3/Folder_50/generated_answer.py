
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1.lower()) == sorted(s2.lower())
    
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 20:
                    return True
    return False
