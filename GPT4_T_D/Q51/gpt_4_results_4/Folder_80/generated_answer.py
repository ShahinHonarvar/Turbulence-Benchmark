
def if_contains_anagrams(strings):
    from collections import Counter

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    def check_if_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        s1 = s1.lower()
        s2 = s2.lower()
        if s1 != s2 and is_anagram(s1, s2):
            return True
        return False

    anagram_pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if check_if_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 255:
                    return False
    return True
