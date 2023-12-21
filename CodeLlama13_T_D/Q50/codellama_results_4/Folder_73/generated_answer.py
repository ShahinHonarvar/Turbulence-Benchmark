
def if_contains_anagrams(my_list):
    anagram_pairs = 0
    for i in range(len(my_list)):
        for j in range(i+1, len(my_list)):
            if sorted([my_list[i], my_list[j]]) == sorted(my_list[i].lower()):
                anagram_pairs += 1
    return anagram_pairs >= 91
