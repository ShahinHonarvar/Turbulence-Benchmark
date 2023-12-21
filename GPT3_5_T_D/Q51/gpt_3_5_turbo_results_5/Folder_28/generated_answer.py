
import collections

def if_contains_anagrams(lst):
    def get_sorted_string(word):
        return ''.join(sorted(word.lower()))

    anagram_count = 0
    anagram_dict = collections.defaultdict(int)

    for word in lst:
        if len(word) >= 3:
            sorted_word = get_sorted_string(word)
            anagram_dict[sorted_word] += 1

    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2

    if anagram_count <= 78:
        return True
    else:
        return False
