
def if_contains_anagrams(strings):
    from collections import Counter
    
    counter_dict = Counter()
    
    for string in strings:
        counter_dict[tuple(sorted(string.lower()))] += 1
    
    anagram_pairs = 0
    
    for count in counter_dict.values():
        if count >= 2:
            anagram_pairs += count * (count - 1) // 2
    
    return anagram_pairs <= 97
