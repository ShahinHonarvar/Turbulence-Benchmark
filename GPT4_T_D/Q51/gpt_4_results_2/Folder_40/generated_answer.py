
def if_contains_anagrams(lst):
    from collections import defaultdict

    def word_key(word):
        return ''.join(sorted(word.lower()))

    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[word_key(word)].append(word)

    pair_count = 0
    for anagram_list in anagrams.values():
        n = len(anagram_list)
        if n > 1:
            pair_count += n * (n - 1) // 2
        if pair_count > 29:
            return False

    return True
