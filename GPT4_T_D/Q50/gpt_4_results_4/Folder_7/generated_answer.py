
def if_contains_anagrams(lst):
    from collections import defaultdict

    def sort_word(word):
        return ''.join(sorted(word.lower()))

    sorted_words = defaultdict(set)

    for word in lst:
        if len(word) >= 3:
            sorted_words[sort_word(word)].add(word.lower())

    count = 0
    for anagrams in sorted_words.values():
        count += len(anagrams) * (len(anagrams) - 1) // 2
        if count >= 178:
            return True
    return False
