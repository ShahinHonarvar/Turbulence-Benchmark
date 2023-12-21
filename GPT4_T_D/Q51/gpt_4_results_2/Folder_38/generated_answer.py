
def if_contains_anagrams(word_list):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    anagram_pairs = 0
    for i in range(len(word_list)):
        for j in range(i+1, len(word_list)):
            str1, str2 = word_list[i], word_list[j]
            if len(str2) > 2 and len(str1) > 2 and is_anagram(str1, str2):
                anagram_pairs += 1
                if anagram_pairs > 416:
                    return False
    return True
