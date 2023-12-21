
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    anagrams = 0
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if len(lst[j]) < 3:
                continue
            if is_anagram(lst[i].lower(), lst[j].lower()):
                anagrams += 1
                if anagrams > 68:
                    return False
    return True
