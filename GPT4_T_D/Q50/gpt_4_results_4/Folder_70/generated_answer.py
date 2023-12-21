
from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    count = 0
    anagram_dict = defaultdict(list)
    
    for word in list_of_strings:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            anagram_dict[sorted_word].append(word)
    
    for anagram in anagram_dict.values():
        n = len(anagram)
        if n > 1:
            count += (n*(n-1))//2

    if count >= 189:
        return True
    else:
        return False
