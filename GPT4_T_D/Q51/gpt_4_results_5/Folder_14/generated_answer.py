
from collections import defaultdict

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def if_contains_anagrams(words_list):
    cnt = 0
    words_dict = defaultdict(list)

    for word in words_list:
        word = word.lower()
        if len(word) >= 3:
            words_dict[''.join(sorted(word))].append(word)
    
    for word, anagrams in words_dict.items():
        if len(anagrams) > 1:
            cnt += len(anagrams) * (len(anagrams) - 1) // 2

    return cnt <= 474
