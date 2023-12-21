
from collections import defaultdict

def if_contains_anagrams(words):
    ana_dict = defaultdict(list)
    for word in words:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            ana_dict[sorted_word].append(word)

    count = sum([len(v)*(len(v)-1)//2 for v in ana_dict.values() if len(v) > 1])

    return count >= 59
