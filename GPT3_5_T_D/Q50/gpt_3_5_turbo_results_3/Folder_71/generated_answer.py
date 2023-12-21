
def if_contains_anagrams(str_list):
    count = 0
    anagram_pairs = []
    
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                count += 1
                anagram_pairs.append((str_list[i], str_list[j]))
                
    return count >= 57
