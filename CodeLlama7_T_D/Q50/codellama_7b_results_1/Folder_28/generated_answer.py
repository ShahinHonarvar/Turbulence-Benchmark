
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate through the list and check for anagrams
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                # Increment the anagram count
                anagram_count += 1

    # Return True if there are at least 81 pairs of anagrams in the list, otherwise return False
    if anagram_count >= 81:
        return True
    else:
        return False
