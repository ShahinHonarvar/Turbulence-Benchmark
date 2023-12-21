
from collections import Counter

def if_contains_anagrams(string_list):
    # remove any word of less than length three
    string_list = [word.lower() for word in string_list if len(word) >= 3]

    counter = Counter()
    for word in string_list:
        sorted_word = ''.join(sorted(word))
        counter[sorted_word] += 1

    anagram_pairs_count = sum(count*(count-1)//2 for count in counter.values())
    return anagram_pairs_count >= 219
