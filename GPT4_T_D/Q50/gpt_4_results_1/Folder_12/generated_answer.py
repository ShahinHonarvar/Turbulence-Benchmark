
def if_contains_anagrams(lst):
    from collections import Counter

    words_map = Counter([''.join(sorted(word.lower())) for word in lst if len(word) >= 3])
    anagrams = sum(count * (count - 1) // 2 for count in words_map.values())
    
    return anagrams >= 69
