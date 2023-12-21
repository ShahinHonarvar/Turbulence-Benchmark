
def if_contains_anagrams(string_list):
    from collections import Counter
    
    def is_anagram(string1, string2):
        if len(string1) != len(string2):
            return False
        count1 = Counter(string1.lower())
        count2 = Counter(string2.lower())
        return count1 == count2
    
    anagram_pairs = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if is_anagram(string_list[i], string_list[j]):
                anagram_pairs += 1
                if anagram_pairs > 65:
                    return False
    return True
