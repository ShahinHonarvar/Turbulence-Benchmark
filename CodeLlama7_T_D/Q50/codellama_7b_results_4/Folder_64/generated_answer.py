
def if_contains_anagrams(my_list):
    # Check if there are at least 5 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                num_pairs += 1
    # Check if the number of pairs is greater than or equal to 5
    return num_pairs >= 5
