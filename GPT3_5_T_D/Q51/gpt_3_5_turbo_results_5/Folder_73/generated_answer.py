
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1.lower()) == sorted(s2.lower())

    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_count += 1
                if anagram_count > 279:
                    return False

    return True
