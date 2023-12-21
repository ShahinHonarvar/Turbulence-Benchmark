
def if_contains_anagrams(my_list):
    anagrams = []
    for s in my_list:
        anagrams += [s[i:] for i in range(len(s)) if s[i:].lower() not in anagrams]
    return len(anagrams) <= 188
