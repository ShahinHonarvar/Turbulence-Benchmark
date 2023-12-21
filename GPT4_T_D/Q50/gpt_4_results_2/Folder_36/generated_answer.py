
def if_contains_anagrams(list_of_strings):
    from itertools import combinations
    anagram_count = 0

    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())

    for str1, str2 in combinations(list_of_strings, 2):
        if is_anagram(str1, str2):
            anagram_count += 1
            if anagram_count >= 312:
                return True
    return False
