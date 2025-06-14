
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    min_length = 3

    # Iterate over the list and check for anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                # Increment the anagram count if both strings are anagrams of each other
                anagram_count += 1

    # Return true if there are at least 85 pairs of anagrams in the list; otherwise, return false
    return anagram_count >= 85
