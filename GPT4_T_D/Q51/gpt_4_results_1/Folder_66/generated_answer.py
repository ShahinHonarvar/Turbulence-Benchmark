
def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        if len(str1)<3 or len(str2)<3:
            return False
        return sorted(str1.lower()) == sorted(str2.lower())

    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                anagram_pairs += 1
            if anagram_pairs > 64:
                return False
    return True
