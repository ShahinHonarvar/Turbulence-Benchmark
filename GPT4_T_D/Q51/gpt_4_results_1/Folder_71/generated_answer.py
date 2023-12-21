
from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    word_count = dict()

    for i in range(len(lst)):
        word = ''.join(sorted(lst[i].lower()))
        if len(word) >= 3:
            if word in word_count:
                word_count[word].append(lst[i])
            else:
                word_count[word] = [lst[i]]
                
    for key in word_count:
        if len(word_count[key]) > 1:
            n = len(word_count[key])
            count += (n*(n-1))//2
            
    return count <= 9
