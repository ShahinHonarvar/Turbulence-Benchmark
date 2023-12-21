
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    min_length = 3

    # Loop through the list and check for anagrams
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                anagram_count += 1

    # Return true if there are at most 116 pairs of anagrams in the list
    return anagram_count <= 116
