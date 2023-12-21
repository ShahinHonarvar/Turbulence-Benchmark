
def if_contains_anagrams(string_list):
    lower_string_list = [string.lower() for string in string_list]
    anagram_pairs = []
    for i in range(len(lower_string_list)):
        for j in range(i+1, len(lower_string_list)):
            if len(lower_string_list[i]) >= 3 and len(lower_string_list[j]) >= 3:
                sorted_i = sorted(lower_string_list[i]) 
                sorted_j = sorted(lower_string_list[j])
                if sorted_i == sorted_j:
                    anagram_pairs.append((lower_string_list[i], lower_string_list[j]))
    return len(anagram_pairs) >= 18
