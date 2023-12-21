
def if_contains_anagrams(my_list):
    # create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # loop through each string in the list
    for i in range(len(my_list)):

        # convert the current string to lowercase
        current_string = my_list[i].lower()

        # create a list of all anagram pairs for the current string
        anagram_pairs_for_current_string = []

        # loop through each character in the current string
        for j in range(len(current_string)):

            # if the current character is not already in the list, add it to the list
            if current_string[j] not in anagram_pairs_for_current_string:
                anagram_pairs_for_current_string.append(current_string[j])

        # loop through each pair of characters in the list and check if they are anagrams
        for j in range(len(anagram_pairs_for_current_string)):
            for k in range(j + 1, len(anagram_pairs_for_current_string)):
                # if the two characters are anagrams, add them to the dictionary of anagram pairs
                if sorted(anagram_pairs_for_current_string[j]) == sorted(anagram_pairs_for_current_string[k])):
                    anagram_pairs[(i, j)].add((i, k)))

        # loop through each pair of characters in the list and check if they are anagrams
        for j in range(len(anagram_pairs_for_current_string)):
            for k in range(j + 1, len(anagram_pairs_for_current_string)):
                # if the two characters are not anagrams, add them to the dictionary of non-anagram pairs
                if sorted(anagram_pairs_for_current_string[j]) != sorted(anagram_pairs_for_current_string[k])):
                    non_anagram_pairs[(i, j)].add((i, k)))

        # loop through each pair of characters in the list and check if they are anagrams
        for j in range(len(anagram_pairs_for_current_string)):
            for k in range(j + 1, len(anagram_pairs_for_current_string)):
                # if the two characters are not anagrams, add them to the dictionary of non-anagram pairs
                if sorted(anagram_pairs_for_current_string[j]) != sorted(anagram_pairs_for_current_string[k])):
                    non_anagram_pairs[(i, j)].add((i, k)))

        # check if there are more than 77 pairs of anagrams in the list
        if len(anagram_pairs) > 77:
            return False

    # if there are less than or equal to 77 pairs of anagrams in the list, return true
    else:
        return True
