
from collections import defaultdict

def if_contains_anagrams(lst):
    def check_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    
    filtered_lst = [i for i in lst if len(i) >= 3]
    anagram_dict = defaultdict(list)
    
    for i, word in enumerate(filtered_lst):
        for next_word in filtered_lst[i+1:]:
            if check_anagram(word, next_word):
                anagram_dict[word].append(next_word)
    
    count = sum([len(v) for v in anagram_dict.values()])
    return count <= 19
