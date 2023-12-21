
def if_contains_anagrams(strings):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)
    
    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count > 5:
                    return False
    return True
