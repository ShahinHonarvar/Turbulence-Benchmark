def if_contains_anagrams(list_of_strings):
    list_of_strings = sorted(list_of_strings)
    list_of_strings.sort()
    anagrams = {}
    for string in list_of_strings:
        letters = set(string.lower())
        for key in anagrams:
            if anagrams[key] == letters:
                anagrams[key] = True
                break
        else:
            anagrams[string.lower()] = True
    return len(anagrams) <= 24
