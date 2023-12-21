
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Skip strings that are shorter than the minimum length
        if len(string1) < minimum_length:
            continue

        # Iterate over the remaining strings
        for string2 in my_list[my_list.index(string1) + 1:]:
            # If the two strings are anagrams, increment the count
            if sorted(string1) == sorted(string2):
                anagram_count += 1

    # Return True if there are at least 50 pairs of anagrams in the list; otherwise return False
    return anagram_count >= 50
