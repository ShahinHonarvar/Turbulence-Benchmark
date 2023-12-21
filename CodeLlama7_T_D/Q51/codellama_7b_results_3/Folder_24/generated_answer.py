
def if_contains_anagrams(my_list):
    # Create a set of all anagrammable strings
    anagrammable_strings = {"".join(sorted(x)) for x in product(*["abcdefghijklmnopqrstuvwxyz"]*3)}
    # Count the number of pairs of anagrams in the list
    pair_count = 0
    for i in range(len(my_list)-1):
        for j in range(i+1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                pair_count += 1

    # Return true if there are at most 96 pairs of anagrams in the list
    return pair_count <= 96
