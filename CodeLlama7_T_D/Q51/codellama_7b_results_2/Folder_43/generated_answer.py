
def if_contains_anagrams(my_list):
    # Check if there are at most 3 pairs of anagrams in the given list
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                pair_count += 1
                if pair_count > 3:
                    return False

    # If there are at most 3 pairs of anagrams in the given list, return True
    else:
        return True
