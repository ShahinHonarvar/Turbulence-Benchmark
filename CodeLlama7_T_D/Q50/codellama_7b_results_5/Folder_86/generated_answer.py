
def if_contains_anagrams(my_list):
    # count the number of pairs of anagrams in the list
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                pair_count += 1
    # return True if there are at least 115 pairs of anagrams in the list; otherwise, return False
    return pair_count >= 115
