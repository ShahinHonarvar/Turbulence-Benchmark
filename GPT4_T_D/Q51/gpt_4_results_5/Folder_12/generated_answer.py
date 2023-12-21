
def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
        
    def pairs(lst):
        pair_count = 0
        for i in range(len(lst) - 1):
            for j in range(i + 1, len(lst)):
                if len(lst[i]) >= 3 and is_anagram(lst[i], lst[j]):
                    pair_count += 1
        return pair_count

    return pairs(lst) <= 92
