
def if_contains_anagrams(strings):
    from collections import Counter
    
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        counter1 = Counter(s1)
        counter2 = Counter(s2)
        return counter1 == counter2
    
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count > 72:
                    return False
    return True
