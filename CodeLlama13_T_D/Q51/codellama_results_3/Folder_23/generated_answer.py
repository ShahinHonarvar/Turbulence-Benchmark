
def if_contains_anagrams(my_list):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    anagrams = []
    for s in my_list:
        ss = "".join(sorted(s.lower()))
        if len(ss) >= 3 and ss not in anagrams:
            anagrams.append(ss)
    return len(anagrams) <= 49
