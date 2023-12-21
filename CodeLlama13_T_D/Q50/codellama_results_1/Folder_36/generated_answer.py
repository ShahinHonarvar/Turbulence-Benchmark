
def if_contains_anagrams(my_list):
    anagrams = []
    for s in my_list:
        anagrams += [[i, j] for i, j in zip(s, reversed(s)) if len(set(i)) == 3 and set(i) == set(j)]
    return len(anagrams) >= 312
