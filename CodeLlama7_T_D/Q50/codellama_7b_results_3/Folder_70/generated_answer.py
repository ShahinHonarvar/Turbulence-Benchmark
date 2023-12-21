
def if_contains_anagrams(my_list):
    # Count the number of anagram pairs in the list
    pair_count = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            # Check if the two strings are anagrams of each other
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                pair_count += 1
    # Return True if there are at least 189 pairs of anagrams in the list, False otherwise
    return pair_count >= 189
