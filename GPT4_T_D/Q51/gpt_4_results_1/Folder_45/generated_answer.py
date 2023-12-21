
from collections import Counter

def if_contains_anagrams(lst):
    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def count_anagrams(lst):
        count = 0
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if is_anagram(lst[i], lst[j]):
                    count += 1
        return count

    def filter_words(lst):
        return [word for word in lst if len(word) >= 3]

    lst = [word.lower() for word in lst]
    lst = filter_words(lst)

    anagrams_count = count_anagrams(lst)
    
    return anagrams_count <= 464
