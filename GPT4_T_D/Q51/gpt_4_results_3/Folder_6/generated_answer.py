
def if_contains_anagrams(string_list):
    from collections import Counter
    
    def count_anagrams(s):
        return Counter(''.join(sorted(s.lower())) for s in string_list if len(s) > 2)
    
    anagram_counter = count_anagrams(string_list)
    
    pairs_count = sum(val * (val - 1) // 2 for val in anagram_counter.values())
    
    return pairs_count <= 86
