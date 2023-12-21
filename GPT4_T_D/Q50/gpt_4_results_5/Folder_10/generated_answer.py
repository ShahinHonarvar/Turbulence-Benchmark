
def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = "".join(sorted(word.lower()))
        if len(word) >= 3:
            if word in anagrams:
                count += anagrams[word]
                anagrams[word] += 1
            else:
                anagrams[word] = 1
    return count >= 52
