
def if_contains_anagrams(lst):
    anagrams = []
    for word1 in lst:
        word1 = word1.lower()
        if len(word1) >= 3:
            for word2 in lst:
                word2 = word2.lower()
                if word1 != word2 and sorted(word1) == sorted(word2):
                    if sorted([word1, word2]) not in anagrams:
                        anagrams.append(sorted([word1, word2]))
    return len(anagrams) <= 210
