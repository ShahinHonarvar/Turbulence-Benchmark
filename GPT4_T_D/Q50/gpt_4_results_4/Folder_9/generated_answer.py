
from collections import defaultdict

def if_contains_anagrams(lst):
    words_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            words_dict[''.join(sorted(word))].append(word)

    anagrams = sum(len(words)>=2 for words in words_dict.values())
    if anagrams >= 66:
        return True
    else:
        return False
