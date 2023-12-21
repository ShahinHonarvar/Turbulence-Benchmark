
def if_contains_anagrams(my_list):
    for s in my_list:
        anagrams = 0
        for t in my_list:
            if len(s) >= 3 and s.lower() == t.lower():
                anagrams += 1
        if anagrams > 279:
            return False
    return True
