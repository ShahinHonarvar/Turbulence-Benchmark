
def if_contains_anagrams(lst):
    from collections import Counter
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)

    pairs = []
    for index1, word1 in enumerate(lst):
        if len(word1) < 3:
            continue
        word1 = word1.lower()
        for index2, word2 in enumerate(lst[index1 + 1:]):
            if len(word2) < 3:
                continue
            word2 = word2.lower()
            if is_anagram(word1, word2):
                pairs.append((index1, index1 + 1 + index2))

    return len(pairs) <= 93
