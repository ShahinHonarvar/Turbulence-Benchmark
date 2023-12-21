
def if_contains_anagrams(my_list):
    anagrams = {}
    for s in my_list:
        key = "".join(sorted(s.lower()))
        if len(key) >= 3 and key not in anagrams:
            anagrams[key] = [s]
        elif len(key) >= 3 and key in anagrams:
            anagrams[key].append(s)
    return len(anagrams) <= 73
