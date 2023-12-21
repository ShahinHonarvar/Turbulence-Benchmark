
def if_contains_anagrams(lst):
    anagrams = {}
    pairs = 0

    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                pairs += anagrams[sorted_word]
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
        if pairs >= 25:
            return True

    return False
