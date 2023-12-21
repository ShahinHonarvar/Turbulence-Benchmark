
def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        if len(word1) != len(word2) or word1.lower() == word2.lower():
            return False
        return sorted(word1.lower()) == sorted(word2.lower())

    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 64:
                    return True
    return False
