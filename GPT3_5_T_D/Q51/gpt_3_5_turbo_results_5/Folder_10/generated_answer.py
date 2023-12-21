
import collections

def if_contains_anagrams(lst):
    counter = collections.Counter()
    anagram_count = 0

    for word in lst:
        if len(word) > 2:
            normalized_word = ''.join(sorted(word.lower()))
            counter[normalized_word] += 1
            if counter[normalized_word] == 2:
                anagram_count += 1

    return anagram_count <= 21
