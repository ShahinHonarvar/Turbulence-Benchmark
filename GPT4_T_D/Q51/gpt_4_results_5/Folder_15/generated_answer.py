
def if_contains_anagrams(list_of_strings):
    anagram_dict = {}
    anagram_pairs = 0
    
    for string in list_of_strings:
        sorted_string = "".join(sorted(string.lower()))
        
        if len(sorted_string) < 3:
            continue
            
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
            
    for val in anagram_dict.values():
        if val > 1:
            anagram_pairs += (val * (val - 1)) // 2
            
    return anagram_pairs <= 20
