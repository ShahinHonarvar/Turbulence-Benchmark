
def if_contains_anagrams(lst):
    import collections
    anagrams = collections.defaultdict(int)
    
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word] += 1
            
    count = 0
    for key in anagrams:
        count += (anagrams[key] * (anagrams[key] - 1)) // 2
    
    return count <= 92
