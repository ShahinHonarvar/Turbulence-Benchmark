
def if_contains_anagrams(lst):
    from collections import Counter

    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) != len(str2) or str1 == str2:
            return False
        return Counter(str1) == Counter(str2)

    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 73:
                    return False
    return True
