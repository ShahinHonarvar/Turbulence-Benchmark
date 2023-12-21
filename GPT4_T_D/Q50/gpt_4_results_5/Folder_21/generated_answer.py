
from collections import defaultdict

def if_contains_anagrams(words):
    words_data = defaultdict(list)

    for word in words:
        word = word.lower()
        key = "".join(sorted(word))
        if len(word) >= 3:
            words_data[key].append(word)
            
    pairs_of_anagrams = sum(len(v)*(len(v)-1)//2 for v in words_data.values())
    if pairs_of_anagrams >= 136:
        return True
    else:
        return False
