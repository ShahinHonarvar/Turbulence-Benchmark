
def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    
    def count_anagrams(lst):
        count = 0
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if len(lst[i]) >= 3 and is_anagram(lst[i], lst[j]):
                    count += 1
        return count
    
    return count_anagrams(lst) <= 74
