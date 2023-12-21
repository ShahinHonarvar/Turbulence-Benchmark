
def if_contains_anagrams(string_list):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagram_pairs = []
    
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if is_anagram(string_list[i], string_list[j]):
                    anagram_pairs.append((string_list[i], string_list[j]))
    
    if len(anagram_pairs) >= 28:
        return True
    else:
        return False
