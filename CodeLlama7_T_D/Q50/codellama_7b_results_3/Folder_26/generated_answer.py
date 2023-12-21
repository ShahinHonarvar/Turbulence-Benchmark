
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    anagram_length = 3

    # Iterate through the list and check for anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                # If the strings are anagrams of each other, increment the anagram count
                anagram_count += 1

    # Check if there are at least 49 pairs of anagrams in the list
    if anagram_count >= 49:
        return True

    else:
        return False
