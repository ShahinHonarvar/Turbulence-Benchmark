
from collections import defaultdict 

def if_contains_anagrams(string_list): 
    sorted_words_dict = defaultdict(list) 
    for word in string_list: 
        if len(word) >= 3: 
            sorted_word = "".join(sorted(word.lower())) 
            sorted_words_dict[sorted_word].append(word) 

    count = 0 
    for word_list in sorted_words_dict.values(): 
        n = len(word_list) 
        count += n*(n-1)//2 

    return count <= 181
