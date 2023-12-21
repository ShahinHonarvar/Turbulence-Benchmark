
def if_contains_anagrams(lst):
    from collections import Counter
    
    def is_anagram(word1, word2):
        return Counter(word1.lower()) == Counter(word2.lower())

    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 89:
                    return True

    return False
