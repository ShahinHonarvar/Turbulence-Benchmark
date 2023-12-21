
def if_contains_anagrams(str_list):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())

    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                if is_anagram(str_list[i], str_list[j]):
                    anagram_pairs += 1
                    if anagram_pairs >= 50:
                        return True
    return False
