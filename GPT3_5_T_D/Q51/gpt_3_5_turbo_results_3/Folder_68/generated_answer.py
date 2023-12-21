
def if_contains_anagrams(strings):
    def are_anagrams(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if are_anagrams(strings[i], strings[j]) and len(strings[i]) >= 3:
                anagram_count += 1
                if anagram_count > 94:
                    return False
    
    return True
