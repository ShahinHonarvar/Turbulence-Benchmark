
def if_contains_anagrams(words):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    for word in words:
        anagram = True
        for letter in english_letters:
            if word.lower().count(letter) != 1:
                anagram = False
                break

        if not anagram:
            return False

    return True
