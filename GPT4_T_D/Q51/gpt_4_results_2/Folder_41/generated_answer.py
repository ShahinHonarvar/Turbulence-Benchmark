
def if_contains_anagrams(lst):
    from collections import Counter
    
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and is_anagram(lst[i], lst[j]):
                count += 1
                if count > 52:
                    return False
    return True
