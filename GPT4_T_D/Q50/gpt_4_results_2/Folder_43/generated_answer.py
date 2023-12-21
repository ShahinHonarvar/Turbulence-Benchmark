
def if_contains_anagrams(words):
    anagrams = {}
    count = 0
    for word in words:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            count += 1
        else:
            anagrams[sorted_word] = 1
    return count >= 61
