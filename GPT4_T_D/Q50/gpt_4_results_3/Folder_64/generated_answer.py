
from collections import defaultdict

def if_contains_anagrams(str_list):
    words_dict = defaultdict(list)
    for word in str_list:
        if len(word) >= 3:
            words_dict[''.join(sorted(word.lower()))].append(word)
        
    pairs_count = sum([len(words)//2 for words in words_dict.values()])
    if pairs_count >= 5:
        return True
    else:
        return False
