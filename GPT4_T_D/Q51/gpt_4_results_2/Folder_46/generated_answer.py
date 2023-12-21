
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    length = len(lst)
    count = 0
    for i in range(length):
        for j in range(i+1, length):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                count += 1
            if count > 61:
                return False
    return True
