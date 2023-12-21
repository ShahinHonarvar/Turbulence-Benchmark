
def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    anagram_pairs = 0
    for i in range(len(strings)-1):
        for j in range(i+1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                
    return True if anagram_pairs >= 70 else False
