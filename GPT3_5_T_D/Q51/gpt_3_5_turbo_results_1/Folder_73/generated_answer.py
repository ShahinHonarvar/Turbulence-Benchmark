
def if_contains_anagrams(lst):
    import itertools
    
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    def count_anagram_pairs(lst):
        count = 0
        for pair in itertools.combinations(lst, 2):
            if is_anagram(pair[0], pair[1]):
                count += 1
        return count
    
    anagram_lst = [word for word in lst if len(word) >= 3]
    return count_anagram_pairs(anagram_lst) <= 279
