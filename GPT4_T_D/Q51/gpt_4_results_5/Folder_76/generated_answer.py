
def if_contains_anagrams(str_list):
    from collections import Counter

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())

    anagram_pairs = 0

    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and is_anagram(str_list[i], str_list[j]):
                anagram_pairs += 1
            if anagram_pairs > 91:
                return False

    return True
