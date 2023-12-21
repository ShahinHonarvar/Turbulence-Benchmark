
def if_contains_anagrams(str_list):
    # Check if there are at most 181 pairs of anagrams in the list
    num_pairs = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            # Check if the two strings are anagrams of each other
            if sorted(str_list[i]) == sorted(str_list[j]):
                num_pairs += 1
    return num_pairs <= 181
