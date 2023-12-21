
def if_contains_anagrams(my_list):
    # Count the number of anagram pairs in the list
    pair_count = 0

    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                pair_count += 1

    # Return true if there are at least 42 anagram pairs in the list, otherwise return false

    return pair_count >= 42
