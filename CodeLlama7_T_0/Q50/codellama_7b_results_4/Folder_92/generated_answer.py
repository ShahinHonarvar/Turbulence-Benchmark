
def if_contains_anagrams(my_list):
    # Check if there are at least two pairs of anagrams in the list
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                pair_count += 1
                if pair_count >= 2:
                    return True

    # If there are no pairs of anagrams in the list, return False

    return False
