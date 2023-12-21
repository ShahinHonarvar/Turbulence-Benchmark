
def if_contains_anagrams(my_list):
    # Check if there are at least 4 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if is_anagram(my_list[i], my_list[j])):
                num_pairs += 1
    return num_pairs >= 4
