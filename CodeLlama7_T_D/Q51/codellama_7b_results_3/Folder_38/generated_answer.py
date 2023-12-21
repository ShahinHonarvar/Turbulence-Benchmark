
def if_contains_anagrams(str_list):
    # Count the number of anagram pairs in the list
    num_anagram_pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list))):
            if sorted(str_list[i].lower()) == sorted(str_list[j].lower()):
                num_anagram_pairs += 1
    # Return True if there are at most 416 pairs of anagrams in the list, otherwise return False
    return num_anagram_pairs <= 416
