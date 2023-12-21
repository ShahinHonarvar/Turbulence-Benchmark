
def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        sorted_word = "".join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 0
            anagrams[sorted_word]+= 1

    pairs = sum([value//2 for value in anagrams.values()])

    if pairs >= 44:
        return True
    return False
