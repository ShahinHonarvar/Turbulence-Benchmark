
def if_contains_anagrams(my_list):
    # count the number of anagram pairs
    pair_count = 0

    for i in range(len(my_list) - 1):

        for j in range(i + 1, len(my_list))):

            if sorted(my_list[i]) == sorted(my_list[j])):

                pair_count += 1

    return pair_count <= 401
