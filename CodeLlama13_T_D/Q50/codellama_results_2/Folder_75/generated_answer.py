
def if_contains_anagrams(str_list):
    anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if str_list[i].lower() == str_list[j].lower():
                continue
            elif sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                anagram_pairs += 1
    return anagram_pairs >= 70
