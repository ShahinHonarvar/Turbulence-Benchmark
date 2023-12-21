
from collections import Counter

def if_contains_anagrams(string_list):
    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    anagram_pairs = 0
    checked = []
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i])>=3 and len(string_list[j])>=3 and \
               string_list[i].lower() not in checked and string_list[j].lower() not in checked:
                if is_anagram(string_list[i], string_list[j]):
                    anagram_pairs += 1
                    checked.append(string_list[i].lower())
                    checked.append(string_list[j].lower())
                
    if anagram_pairs<=188:
        return True
    else:
        return False
