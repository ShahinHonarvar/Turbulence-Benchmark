
from collections import defaultdict

def if_contains_anagrams(lst):
    word_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_dict[''.join(sorted(word.lower()))].append(word)
    counter = sum([len(values)*(len(values)-1)//2 for values in word_dict.values()])
    return counter >= 78
