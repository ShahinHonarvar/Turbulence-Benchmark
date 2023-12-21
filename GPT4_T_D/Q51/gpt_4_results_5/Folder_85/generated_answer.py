
from collections import defaultdict

def if_contains_anagrams(str_list):
    len_list = len(str_list)
    anagram_count = 0
    
    for i in range(len_list):
        str_list[i] = str_list[i].lower()
      
    anagram_dict = defaultdict(list)
   
    for ind, word in enumerate(str_list):
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
 
    for value in anagram_dict.values():
        if len(value) >= 2 and len(value[0]) >= 3:
            anagram_count = anagram_count + (len(value) * (len(value)-1)) // 2

    if anagram_count <= 276:
        return True
    else:
        return False
