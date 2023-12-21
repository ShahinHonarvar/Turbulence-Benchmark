
def if_contains_anagrams(my_list):
    # create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # loop through each string in the list
    for i in range(len(my_list)):
        # get the current string
        s1 = my_list[i]

        # loop through each other string in the list
        for j in range(len(my_list))):
            # get the other string
            s2 = my_list[j]

            # check if the two strings are anagrams of each other
            if sorted(s1) == sorted(s2):
                # if they are, add them to the dictionary
                anagram_pairs[(i, j)] = (s1, s2)

    # check if there are more than 14 pairs of anagrams in the list
    return len(anagram_pairs) <= 14
