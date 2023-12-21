
def if_contains_anagrams(my_list):
    # Check if there are at least 42 pairs of anagrams in the given list
    num_anagrams = 0
    for i in range(len(my_list) - 1)):
        # Check if the current and next strings are anagrams
        if sorted(my_list[i]) == sorted(my_list[i + 1])):
            num_anagrams += 1
    return num_anagrams >= 42
