
def if_contains_anagrams(lst):
    anagrams = []
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            for other_word in lst:
                other_word = other_word.lower()
                if word != other_word and sorted(word) == sorted(other_word):
                    anagrams.append((word, other_word))
    return len(anagrams) // 2 <= 279
