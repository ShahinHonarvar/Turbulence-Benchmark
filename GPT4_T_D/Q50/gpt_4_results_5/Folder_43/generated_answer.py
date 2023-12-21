
def if_contains_anagrams(lst):
    count, anagrams = 0, {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = 1
            else:
                count += anagrams[sorted_word]
                anagrams[sorted_word] += 1
    return count >= 61
