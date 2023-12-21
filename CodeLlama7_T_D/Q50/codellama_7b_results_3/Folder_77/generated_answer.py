
def if_contains_anagrams(my_list):
    # count the number of anagram pairs
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            # check if the two strings are anagrams
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_pairs += 1
                if num_pairs >= 209:
                    return True

    return False
