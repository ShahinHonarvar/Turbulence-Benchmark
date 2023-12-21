
import collections

def if_contains_anagrams(strings):
    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        if len(str1) < 3 or len(str2) < 3 or len(set(str1) - set('abcdefghijklmnopqrstuvwxyz')) > 0 or len(set(str2) - set('abcdefghijklmnopqrstuvwxyz')) > 0:
            return False
        return collections.Counter(str1) == collections.Counter(str2)

    anagram_pairs = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 47:
                    return False
    return True
