
def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        if len(word1) != len(word2):
            return False
        word1 = word1.lower()
        word2 = word2.lower()
        return sorted(word1) == sorted(word2)

    count = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 60:
                    return False
    return True
