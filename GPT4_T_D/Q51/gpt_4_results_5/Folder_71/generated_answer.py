
from collections import Counter

def if_contains_anagrams(list_of_strings):
    
    anagram_dict = {}
    
    for word in list_of_strings:
        word = word.lower()
        if len(word) > 2:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    
    pair_count = 0
    for word in anagram_dict:
        anagram_list = anagram_dict[word]
        if len(anagram_list) > 1:
            count_dict = Counter(anagram_list)
            for count in count_dict.values():
                if count >= 2:
                    pair_count += 1
                    if pair_count > 9:
                        return False
                    
    return True
