
def if_contains_anagrams(strings):
    anagram_count = 0
    
    def is_anagram(string1, string2):
        sorted1 = sorted(string1.lower())
        sorted2 = sorted(string2.lower())
        return sorted1 == sorted2
    
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_count += 1
                
                if anagram_count > 22:
                    return False
    
    return True
