
def if_contains_anagrams(word_list):
    count = 0
    checked = []

    def is_anagram(word1, word2):
        if len(word1) < 3 or len(word2) < 3:
            return False
        return sorted(word1.lower()) == sorted(word2.lower())

    for word in word_list:
        for checked_word in checked:
            if is_anagram(word, checked_word):
                count += 1
        checked.append(word)

    return count >= 314
