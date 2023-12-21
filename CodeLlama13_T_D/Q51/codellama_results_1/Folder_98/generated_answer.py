
def if_contains_anagrams(my_list):
    anagram_pairs = 0
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if (sorted(my_list[i].lower()) == sorted(my_list[j].lower())) and len(my_list[i]) >= 3:
                anagram_pairs += 1
    return anagram_pairs <= 46
