
from collections import defaultdict

def if_contains_anagrams(lst):
    freq = defaultdict(list)
    
    for word in lst:
        if len(word)>=3:
            word = "".join(sorted(word.lower()))
            freq[word].append(word)
            
    count = 0
    for val in freq.values():
        cnt = len(val)
        if cnt>1:
            count += cnt*(cnt-1)//2
            
    return count <= 36
