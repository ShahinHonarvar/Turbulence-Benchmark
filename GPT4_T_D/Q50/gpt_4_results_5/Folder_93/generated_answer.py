
def if_contains_anagrams(lst):   
    anagrams = {}
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = "".join(sorted(word_lower))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word_lower)
            else:
                anagrams[sorted_word] = [word_lower]
    
    pair_count = sum(len(words)//2 for words in anagrams.values())
    return pair_count >= 18
