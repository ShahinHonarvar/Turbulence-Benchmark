
def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    return count >= 42
