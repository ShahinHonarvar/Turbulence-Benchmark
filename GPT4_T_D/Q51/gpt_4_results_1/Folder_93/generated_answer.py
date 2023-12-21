
def if_contains_anagrams(lst):
    from collections import Counter
    pairs = 0

    def is_anagram(str1, str2):
        if len(str1) < 3 or len(str2) < 3:
            return False
        return Counter(str1.lower()) == Counter(str2.lower())

    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                pairs += 1
                if pairs > 36:
                    return False
    return True
