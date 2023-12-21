
def if_contains_anagrams(my_list):
    anagrams = set()
    for word in my_list:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams.add(key)
    return len(anagrams) >= 52
