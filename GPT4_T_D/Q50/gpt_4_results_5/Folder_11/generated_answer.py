
from collections import Counter
def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    count = 0
    for key, values in anagram_dict.items():
        if len(values) > 1:
            val_count = Counter(values)
            for x in val_count.values():
                if x > 1:
                    count += x*(x-1)//2
    return count >= 28
