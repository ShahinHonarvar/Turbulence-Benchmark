
def if_contains_anagrams(str_list):
    # Count the number of pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list))):
            if sorted(str_list[i]) == sorted(str_list[j])):
                num_pairs += 1
    return num_pairs >= 61
