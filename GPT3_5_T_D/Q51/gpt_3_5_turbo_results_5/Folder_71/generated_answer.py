
def if_contains_anagrams(strings):
    def count_letters(string):
        letters = [0] * 26
        for char in string.lower():
            if char.isalpha():
                letters[ord(char) - ord('a')] += 1
        return tuple(letters)

    anagram_count = 0
    for i in range(len(strings)):
        if len(strings[i]) >= 3:
            for j in range(i+1, len(strings)):
                if len(strings[j]) >= 3:
                    if count_letters(strings[i]) == count_letters(strings[j]):
                        anagram_count += 1
                        if anagram_count > 9:
                            return False
    return True
