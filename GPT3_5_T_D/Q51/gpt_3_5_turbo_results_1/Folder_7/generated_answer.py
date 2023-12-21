
def if_contains_anagrams(lst):
    from collections import Counter

    def is_anagram(a, b):
        return Counter(a.lower()) == Counter(b.lower())

    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagram_count += 1

            if anagram_count > 445:
                return False

    return True
