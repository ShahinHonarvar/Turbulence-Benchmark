
def if_contains_anagrams(word_list):
    from collections import defaultdict
    
    sorted_words = defaultdict(list)
    for word in word_list:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            sorted_words[sorted_word].append(word)

    counter = 0
    for words in sorted_words.values():
        if len(words) > 1:
            counter += 1
            
    return counter >= 26
