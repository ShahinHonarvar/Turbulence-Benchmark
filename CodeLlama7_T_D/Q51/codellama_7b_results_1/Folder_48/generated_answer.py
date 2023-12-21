
def if_contains_anagrams(strings):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    anagram_pairs = set()
    for string in strings:
        letters = [char.lower() for char in string]
        if len(letters) < 3:
            continue

        anagrams = []

        for letter in english_letters:
            if letter not in letters:
                continue

            anagram = "".join(sorted(letters))

            if anagram not in anagrams:
                anagrams.append(anagram)

        if len(anagrams) > 277:
            return False

    return True
