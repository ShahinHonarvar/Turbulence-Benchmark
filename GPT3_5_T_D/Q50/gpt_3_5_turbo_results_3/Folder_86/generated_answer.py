
def if_contains_anagrams(string_list):
    from collections import Counter
    
    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())
    
    count = 0
    
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and is_anagram(string_list[i], string_list[j]):
                count += 1
                
    return count >= 115
