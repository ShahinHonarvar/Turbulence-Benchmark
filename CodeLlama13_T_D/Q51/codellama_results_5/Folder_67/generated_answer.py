
def if_contains_anagrams(my_list):
    anagrams = {}
    for word in my_list:
        key = ''.join(sorted(word))
        if key not in anagrams:
            anagrams[key] = [word]
        else:
            anagrams[key].append(word)
    return len(anagrams.values()) <= 5
