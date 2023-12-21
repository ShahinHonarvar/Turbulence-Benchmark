
def if_contains_anagrams(lst):
    from collections import Counter
    anagrams = []

    for word in lst:
        word = word.lower()
        if len(word) < 3:
            continue
        found = False
        wordCounter = Counter(word)
        for anagram in anagrams:
            if Counter(anagram) == wordCounter:
                found = True
                break
        if not found:
            anagrams.append(word)
    return len(anagrams) <= 78
