
def if_contains_anagrams(list_of_strings):
    anagrams = set()
    for word in list_of_strings:
        word = word.lower()
        if len(word) >= 3 and word[1:-1] not in anagrams:
            anagrams.add(word)
    return len(anagrams) <= 116
