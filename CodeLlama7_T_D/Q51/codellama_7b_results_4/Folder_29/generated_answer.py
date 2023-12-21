
def if_contains_anagrams(my_list):
    # check if the list is empty
    if len(my_list) == 0:
        return False

    # create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # loop through each string in the list
    for s1 in my_list:

        # loop through each string in the list again
        for s2 in my_list:

            # check if the strings are not equal and have at least three letters
            if s1 != s2 and len(s1) >= 3:

                # convert both strings to lowercase and sort the characters
                s1 = ''.join(sorted(s1.lower()))
                s2 = ''.join(sorted(s2.lower()))

                # check if the sorted strings are anagrams of each other
                if s1 == s2:

                    # add the pair to the dictionary
                    anagram_pairs[s1] = s2

        # check if there are at most 318 pairs of anagrams in the list
        if len(anagram_pairs) <= 318:

            # return true if there are at most 318 pairs of anagrams in the list
            return True

    # return false if there are more than 318 pairs of anagrams in the list
    return False
