
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    pairs_count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                pairs_count += 1
                if pairs_count > 445:
                    return False
    return True
