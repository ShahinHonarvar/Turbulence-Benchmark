
def if_contains_anagrams(lst):
    from collections import defaultdict
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    anagram_pairs = defaultdict(list)
    
    for word in lst:
        if len(word) < 3:
            continue
        word_lower = ''.join(sorted([char.lower() for char in word if char.lower() in alphabets]))
        anagram_pairs[word_lower].append(word)
    
    anagram_counts = [len(words) for key, words in anagram_pairs.items() if len(words) > 1]
    
    pair_counts = sum([count * (count - 1) // 2 for count in anagram_counts])
    
    return pair_counts <= 49
