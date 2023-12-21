
def if_contains_anagrams(list_of_str):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
        
    anagram_pairs = 0
    for i in range(len(list_of_str)):
        for j in range(i+1, len(list_of_str)):
            if len(list_of_str[i]) >= 3 and len(list_of_str[j]) >= 3 and is_anagram(list_of_str[i], list_of_str[j]):
                anagram_pairs += 1
            if anagram_pairs > 423:
                return False
    return True
