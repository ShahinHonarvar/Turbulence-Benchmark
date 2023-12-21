
def if_contains_anagrams(lst):
    def count_anagrams(word):
        count = 0
        sorted_word = sorted(word.lower())
        for w in lst:
            if w.lower() != word.lower() and len(w) >= 3 and sorted(w.lower()) == sorted_word:
                count += 1
        return count
    
    pair_count = 0
    for word in lst:
        pair_count += count_anagrams(word) // 2
        
    return pair_count <= 41
