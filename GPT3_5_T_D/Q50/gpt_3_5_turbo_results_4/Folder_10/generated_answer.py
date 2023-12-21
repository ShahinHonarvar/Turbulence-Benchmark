
def if_contains_anagrams(string_list):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())
    
    count = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3 and is_anagram(string_list[i], string_list[j]):
                count += 1
            if count >= 52:
                return True
    return False
