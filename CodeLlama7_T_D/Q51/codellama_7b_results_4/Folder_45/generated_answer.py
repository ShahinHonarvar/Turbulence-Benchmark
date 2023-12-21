
def if_contains_anagrams(my_list):
    # Check if there are at most 464 pairs of anagrams in the given list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                num_pairs += 1
    return num_pairs <= 464
