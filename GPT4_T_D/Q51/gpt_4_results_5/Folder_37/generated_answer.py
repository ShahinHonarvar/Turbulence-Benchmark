
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = dict()
    for word in lst: 
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
                
    pairs = 0
    for key in anagram_dict:
        count_dict = Counter(anagram_dict[key])
        for val in count_dict.values():
            pairs += (val * (val - 1)) // 2
          
    if pairs <= 206:
        return True
    else:
        return False
