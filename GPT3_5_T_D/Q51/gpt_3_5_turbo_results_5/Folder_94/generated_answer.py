
def if_contains_anagrams(lst):
    def is_anagram(a, b):
        return sorted(a.lower()) == sorted(b.lower())
    
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3 and len(lst[j]) >= 3:
                count += 1
                if count > 181:
                    return False
                    
    return True
