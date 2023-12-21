
def if_contains_anagrams(my_list):
    # count the number of anagram pairs in the list
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                pair_count += 1
                # check if the number of anagram pairs is greater than or equal to 74
                if pair_count >= 74:
                    return True
            else:
                continue

    # if no anagram pairs are found, return false

    return False
