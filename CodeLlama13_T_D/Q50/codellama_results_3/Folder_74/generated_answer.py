
def if_contains_anagrams(my_list):
    anagram_pairs = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if my_list[i].lower() == my_list[j].lower():
                continue
            if sorted(my_list[i]) == sorted(my_list[j]):
                anagram_pairs += 1
    return anagram_pairs >= 17
