
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    min_length = 3

    # Iterate through the list and count the number of anagram pairs
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                anagram_pairs += 1
                if anagram_pairs > 54:
                    return False

    # If there are at most 54 pairs of anagrams in the list, return True
    if anagram_pairs <= 54:
        return True

    # Otherwise, return False
    else:
        return False
