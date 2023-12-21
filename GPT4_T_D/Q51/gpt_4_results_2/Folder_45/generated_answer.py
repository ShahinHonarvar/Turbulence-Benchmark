
from collections import defaultdict

def if_contains_anagrams(lst):
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
      
    def count_anagram_pairs(lst):
        count = 0
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if is_anagram(lst[i], lst[j]):
                    count += 1
        return count

    def filter_and_convert(lst):
        filtered_list = list(filter(lambda x: len(x) >= 3, lst)) 
        converted_list = [x.lower() for x in filtered_list]
        return converted_list

    lst = filter_and_convert(lst)
    anagram_count = count_anagram_pairs(lst)

    return anagram_count <= 464
