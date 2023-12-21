
def if_contains_anagrams(lst):
    def count_anagrams(word):
        result = 0
        for i in range(len(lst)):
            if sorted(word.lower()) == sorted(lst[i].lower()) and len(word) >= 3 and len(lst[i]) >= 3:
                result += 1
        return result
    
    anagram_pairs = 0
    for i in range(len(lst)):
        anagram_pairs += count_anagrams(lst[i])
        if anagram_pairs > 210:
            return False
    return True
