
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            return False
        return True

    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count > 69:
                    return False
    return True
