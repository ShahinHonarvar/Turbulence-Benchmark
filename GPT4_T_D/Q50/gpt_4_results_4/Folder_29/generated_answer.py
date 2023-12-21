
def if_contains_anagrams(lst):
    anagrams = dict()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams[sorted_word] += 1
            else:
                anagrams[sorted_word] = 1
    counter = 0
    for key in anagrams:
        counter += anagrams[key] * (anagrams[key]-1) // 2
    return counter >= 35
