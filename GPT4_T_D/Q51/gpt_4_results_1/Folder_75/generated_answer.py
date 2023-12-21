
def if_contains_anagrams(lst):
    from collections import Counter
    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)

    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i].lower(), lst[j].lower()):
                pairs += 1
            if pairs > 55:
                return False
    return True
