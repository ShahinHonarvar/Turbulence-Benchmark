
from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)

    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
            
    counter = sum(len(words)*(len(words)-1)//2 for words in anagrams.values())
    
    if counter <= 407:
        return True
    else:
        return False
