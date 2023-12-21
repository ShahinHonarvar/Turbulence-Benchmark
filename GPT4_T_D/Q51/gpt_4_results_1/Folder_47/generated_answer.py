
def if_contains_anagrams(lst):
    from collections import Counter
    anagram_pairs = []
    
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            anagram_pairs.append(sorted_word)
     
    counter = Counter(anagram_pairs)
    output = sum(val * (val - 1) // 2 for val in counter.values())
    
    if output <= 366:
        return True
    else:
        return False
