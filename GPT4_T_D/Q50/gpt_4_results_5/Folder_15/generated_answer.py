
def if_contains_anagrams(strings):
    from collections import defaultdict

    def _is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    word_dict = defaultdict(list)

    for word in strings:
        if len(word) < 3:
            continue
        word_dict[''.join(sorted(word.lower()))].append(word)
   
    count = sum([1 for words in word_dict.values() if len(words) > 1])

    return count >= 4
