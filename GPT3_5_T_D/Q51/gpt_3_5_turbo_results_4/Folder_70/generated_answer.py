
def if_contains_anagrams(lst):
    def is_anagram(word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3 and len(word2) >= 3

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 97:
                    return False
    return True
