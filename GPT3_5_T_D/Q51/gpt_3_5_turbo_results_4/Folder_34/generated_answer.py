
def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        if len(word1) < 3 or len(word2) < 3:
            return False
        sorted_word1 = sorted(word1.lower())
        sorted_word2 = sorted(word2.lower())
        if sorted_word1 == sorted_word2:
            return True
        return False

    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 401:
                    return False
    return True
