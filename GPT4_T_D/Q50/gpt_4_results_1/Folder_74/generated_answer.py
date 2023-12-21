
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    count = 0
    size = len(lst)
    for i in range(size):
        if len(lst[i]) < 3:
            continue
        for j in range(i+1, size):
            if len(lst[j]) < 3:
                continue
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 17:
                    return True
    return False
