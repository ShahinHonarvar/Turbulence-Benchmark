
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    minimum_length = 3

    # Loop through the list of strings
    for string1 in my_list:
        for string2 in my_list:
            # If the strings are not the same and have at least three letters in common, check if they are anagrams
            if string1 != string2 and len(set(string1) & set(string2))) >= minimum_length:
                # Check if the two strings are anagrams
                if sorted(string1) == sorted(string2):
                    # Increment the number of anagram pairs found
                    anagram_pairs += 1

    # Return True if there are at most three pairs of anagrams in the list, False otherwise
    return anagram_pairs <= 34
