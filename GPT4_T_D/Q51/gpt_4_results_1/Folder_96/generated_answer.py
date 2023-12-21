
def if_contains_anagrams(lst):
    import collections

    def is_anagram(s1, s2):
        return collections.Counter(s1.lower()) == collections.Counter(s2.lower())

    pairs = 0
    for i in range(len(lst) - 1):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                pairs += 1
                if pairs > 2:
                    return False
    return True
