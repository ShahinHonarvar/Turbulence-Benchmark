
def if_contains_anagrams(lst):
    import collections
   
    def is_anagram(word1, word2):
        word1 = word1.lower()
        word2 = word2.lower()
        return sorted(word1) == sorted(word2)

    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i], lst[j]):
                count += 1
                if count > 66:
                    return False
    
    return True
