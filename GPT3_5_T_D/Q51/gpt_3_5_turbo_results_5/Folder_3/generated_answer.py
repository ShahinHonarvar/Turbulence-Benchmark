
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        if len(s1) != len(s2):
            return False
        s1 = s1.lower()
        s2 = s2.lower()
        return sorted(s1) == sorted(s2)

    anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagrams += 1
                if anagrams > 66:
                    return False
    return True
