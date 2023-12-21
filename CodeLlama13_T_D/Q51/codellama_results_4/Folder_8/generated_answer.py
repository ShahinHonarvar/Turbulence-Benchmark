
def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for word in list_of_strings:
        key = ''.join(sorted(word.lower()))
        if key not in anagrams:
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)
    return len(anagrams) <= 68
