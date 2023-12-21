
def if_contains_anagrams(strings):
    def count_letters(word):
        letters = [0] * 26
        for char in word:
            if char.isalpha():
                letters[ord(char.lower()) - ord('a')] += 1
        return tuple(letters)

    anagram_pairs = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if count_letters(strings[i]) == count_letters(strings[j]):
                    anagram_pairs.add((strings[i], strings[j]))

    return len(anagram_pairs) <= 52
