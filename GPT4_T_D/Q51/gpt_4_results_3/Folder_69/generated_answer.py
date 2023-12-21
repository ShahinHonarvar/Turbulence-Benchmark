
from collections import Counter

def if_contains_anagrams(my_list):
    
    def check_anagram(str1, str2):
        
        return Counter(str1) == Counter(str2)
    
    my_list = [str.lower() for str in my_list if len(str)>=3]
    anagram_count = 0
    
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            
            if check_anagram(my_list[i], my_list[j]):
                anagram_count += 1

    return anagram_count <= 58
