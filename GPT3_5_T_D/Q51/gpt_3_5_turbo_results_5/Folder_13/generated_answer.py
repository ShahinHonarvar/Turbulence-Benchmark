
def if_contains_anagrams(lst):
    def count_chars(word):
        return [word.lower().count(char) for char in 'abcdefghijklmnopqrstuvwxyz']

    def are_anagrams(word1, word2):
        return count_chars(word1) == count_chars(word2)

    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and are_anagrams(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 54:
                    return False

    return True
