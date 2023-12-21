
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        str1 = str1.lower()
        str2 = str2.lower()
        return sorted(str1) == sorted(str2)

    anagram_pairs = defaultdict(list)

    for str1 in lst:
        if len(str1) < 3:
            continue
        for str2 in lst:
            if str1 == str2:
                continue
            if is_anagram(str1, str2):
                if str2 not in anagram_pairs[str1] and str1 not in anagram_pairs[str2]:
                    anagram_pairs[str1].append(str2)

    return len(anagram_pairs) <= 43
