
def if_contains_anagrams(my_list):
    # check if there are at least 6 pairs of anagrams in the list
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                pair_count += 1
                if pair_count >= 6:
                    return True
    return False
