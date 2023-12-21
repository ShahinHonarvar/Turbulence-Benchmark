
def if_contains_anagrams(str_list):
    from collections import defaultdict
    
    anagram_count = 0
    
    def normalize(s):
        return ''.join(sorted(s.lower()))
    
    anagrams = defaultdict(int)
    
    for s in str_list:
        if len(s) >= 3:
            anagrams[normalize(s)] += 1
    
    for count in anagrams.values():
        if count >= 2:
            anagram_count += count * (count - 1) // 2
    
    if anagram_count >= 79:
        return True
    else:
        return False
