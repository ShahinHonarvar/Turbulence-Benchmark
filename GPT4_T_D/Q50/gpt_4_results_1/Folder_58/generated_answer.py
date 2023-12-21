
def if_contains_anagrams(lst):
    from collections import defaultdict
    def convert_word(word):
        return ''.join(sorted(word.lower()))

    words_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3: 
            sorted_word = convert_word(word)
            words_dict[sorted_word].append(word)
    
    anagram_count = 0
    for word_list in words_dict.values():
        if len(word_list) >= 2:
            anagram_count += (len(word_list)*(len(word_list)-1))//2

    return anagram_count >= 411
