
def if_contains_anagrams(lst):
    from collections import Counter

    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower()) and len(word1) >= 3

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 65:
                    return False
    return True
