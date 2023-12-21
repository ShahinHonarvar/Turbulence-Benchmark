
def if_contains_anagrams(words):
    from collections import defaultdict
    anagrams = defaultdict(list)
    
    # Finding all potential anagrams
    for word in words:
        if len(word) >= 3:
            # storing word and sorted version of the word
            sorted_word = "".join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    
    # Counting anagram pairs
    pairs = 0
    for word_list in anagrams.values():
        pairs += len(word_list) * (len(word_list) - 1) // 2

    return pairs >= 48
