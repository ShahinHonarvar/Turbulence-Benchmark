
def if_contains_anagrams(my_list):
    anagrams = []
    for word in my_list:
        key = ''.join(sorted(word.lower()))
        if key not in anagrams:
            anagrams.append(key)
    return len(anagrams) <= 17
