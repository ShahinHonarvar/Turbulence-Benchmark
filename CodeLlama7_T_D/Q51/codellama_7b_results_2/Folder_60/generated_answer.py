
def if_contains_anagrams(my_list):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(my_list)):
        # Check if the current string is an anagram of another string in the list
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                num_anagrams += 1
    # Return true if there are at most 77 pairs of anagrams in the list, otherwise return false
    return num_anagrams <= 77
