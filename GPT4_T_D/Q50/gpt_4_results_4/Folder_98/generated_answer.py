
def if_contains_anagrams(string_list):
    from collections import defaultdict
    word_dict = defaultdict(list)
    anagram_pairs = 0
    
    for word in string_list:
        word = word.lower()
        sorted_word = ''.join(sorted(word))
        if len(word) >= 3:            
            word_dict[sorted_word].append(word)
    
    for words in word_dict.values():
        if len(set(words)) > 1:
            anagram_pairs += 1
    
    if anagram_pairs >= 7:
        return True
    else:
        return False
