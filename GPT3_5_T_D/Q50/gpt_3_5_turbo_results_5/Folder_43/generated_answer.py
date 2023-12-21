
def if_contains_anagrams(strings):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower())

    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and is_anagram(strings[i], strings[j]):
                count += 1
                if count >= 61:
                    return True
    return False
