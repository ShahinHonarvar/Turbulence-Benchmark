
def if_contains_anagrams(strings):
    def count_letters(word):
        letters = [0] * 26
        for char in word:
            if char.isalpha():
                index = ord(char.lower()) - ord('a')
                letters[index] += 1
        return tuple(letters)

    anagrams = {}
    for word in strings:
        if len(word) < 3:
            continue
        letters = count_letters(word)
        if letters in anagrams:
            anagrams[letters].append(word)
        else:
            anagrams[letters] = [word]

    count = 0
    for group in anagrams.values():
        if len(group) >= 2:
            count += (len(group) * (len(group) - 1)) // 2

    return count >= 24
