
def if_contains_anagrams(lst):
    from collections import Counter

    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())

    anagrams_count = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                anagrams_count += 1
                if anagrams_count > 41:
                    return False
    return True
