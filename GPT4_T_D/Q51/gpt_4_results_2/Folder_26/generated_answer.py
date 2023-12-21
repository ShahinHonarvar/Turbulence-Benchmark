
def if_contains_anagrams(lst):
    from collections import Counter

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)

    pairs = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            s1 = lst[i].lower()
            s2 = lst[j].lower()
            if len(s1)>=3 and len(s2)>=3 and is_anagram(s1, s2):
                pairs += 1
            if pairs > 35:
                return False
    return True
