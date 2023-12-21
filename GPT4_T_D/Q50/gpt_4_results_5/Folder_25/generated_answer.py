
def if_contains_anagrams(lst):
    from collections import defaultdict

    words = defaultdict(set)
    
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            words[''.join(sorted(word_lower))].add(word_lower)
            
    anagrams = [words for words in words.values() if len(words) > 1]
    
    pairs = sum(len(words) * (len(words) - 1) / 2 for words in anagrams)
    
    return True if pairs >= 14 else False
