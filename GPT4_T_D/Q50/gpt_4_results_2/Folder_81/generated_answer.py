
def if_contains_anagrams(strings):
    anagram_dict = {}
    
    for string in strings:
        sorted_string = "".join(sorted(string.lower()))
        
        if len(sorted_string) < 3:
            continue
            
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
        else:
            anagram_dict[sorted_string] = [string]
            
    pair_count = sum([len(value) * (len(value) - 1) // 2 for key, value in anagram_dict.items()])

    return pair_count >= 16
