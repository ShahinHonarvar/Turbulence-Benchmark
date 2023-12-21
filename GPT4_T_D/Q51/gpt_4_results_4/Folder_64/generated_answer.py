
def if_contains_anagrams(str_list):
    from itertools import combinations
    from collections import Counter
    
    def is_anagram(str1, str2):
        return (Counter(str1) == Counter(str2))

    anagram_count = 0
    str_list = [str_.lower() for str_ in str_list if len(str_) >= 3]

    for str1, str2 in combinations(str_list, 2):
        if is_anagram(str1, str2):
            anagram_count += 1
            if anagram_count > 59:
                return False

    return True
