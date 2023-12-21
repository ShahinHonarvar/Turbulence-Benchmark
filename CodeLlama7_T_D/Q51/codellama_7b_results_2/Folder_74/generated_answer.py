
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list and check for anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            # Check if the current string is an anagram of the previous one
            if sorted(my_list[j].lower()) == sorted(my_list[i].lower()):
                # If it is an anagram, increase the anagram count
                anagram_count += 1

    # Return True if there are at most 57 pairs of anagrams in the given list; otherwise, return False
    return anagram_count <= 57
