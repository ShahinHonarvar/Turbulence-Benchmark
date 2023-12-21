
from collections import defaultdict

def if_contains_anagrams(lst):
    def generate_pairs(lst):
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                yield (lst[i], lst[j])
                
    def is_anagram(str1, str2):
        return len(str1) >= 3 and len(str2) >= 3 and sorted(str1.lower()) == sorted(str2.lower())
    
    cnt = defaultdict(int)
    for pair in generate_pairs(lst):
        if is_anagram(*pair):
            cnt[pair] += 1
    return sum(count >= 2 for count in cnt.values()) >= 75
