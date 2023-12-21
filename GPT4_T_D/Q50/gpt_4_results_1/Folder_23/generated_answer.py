
def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word] = anagrams.get(sorted_word, 0) + 1
    pairs = 0
    for count in anagrams.values():
        pairs += count // 2
    if pairs >= 67:
        return True
    else:
        return False
