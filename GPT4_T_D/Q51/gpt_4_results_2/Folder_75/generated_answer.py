
def if_contains_anagrams(input_list):
    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())
    
    anagram_pair_count = 0
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if is_anagram(input_list[i], input_list[j]):
                anagram_pair_count += 1
                if anagram_pair_count > 55:
                    return False
    return True
