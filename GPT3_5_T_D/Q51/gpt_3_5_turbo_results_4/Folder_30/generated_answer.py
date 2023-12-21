
def if_contains_anagrams(lst):
    def are_anagrams(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        if word1 == word2:
            return False
        return sorted(word1) == sorted(word2)

    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                count += 1
                if count > 28:
                    return False
    return True
