
def if_contains_anagrams(my_list):
    # Count the number of pairs of anagrams in the list
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                pair_count += 1
                    # If the number of pairs of anagrams is greater than 52, return False
                if pair_count > 52:
                    return False
    return True
