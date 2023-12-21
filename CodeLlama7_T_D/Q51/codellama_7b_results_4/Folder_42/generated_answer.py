
def if_contains_anagrams(words):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    anagram_count = 0
    for word in words:
        # Check if the word contains at least three letters
        if len(word) < 3:
            continue

        # Convert the word to lowercase
        word = word.lower()

        # Check if the word is an anagram of the English letters
        if sorted(word) == sorted(english_letters):
            anagram_count += 1
            if anagram_count > 38:
                return False

    return True
