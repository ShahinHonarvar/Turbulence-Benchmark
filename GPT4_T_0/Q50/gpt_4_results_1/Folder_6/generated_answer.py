
from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    count = 0
    for value in anagram_dict.values():
        if len(value) > 1:
            count += Counter(value).most_common(1)[0][1] // 2
    return count >= 26
