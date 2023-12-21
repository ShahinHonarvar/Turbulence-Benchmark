
def if_contains_anagrams(lst):
    from collections import Counter
    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())

    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagrams_count += 1
                if anagrams_count >= 277:
                    return True
    return False
