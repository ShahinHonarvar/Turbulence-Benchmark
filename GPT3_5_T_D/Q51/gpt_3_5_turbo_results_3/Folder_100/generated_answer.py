
def if_contains_anagrams(str_list):
    count = 0
    
    def count_anagrams(word1, word2):
        if sorted(word1.lower()) == sorted(word2.lower()):
            return True
        return False
    
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                if count_anagrams(str_list[i], str_list[j]):
                    count += 1
                    if count > 98:
                        return False
    
    return True
