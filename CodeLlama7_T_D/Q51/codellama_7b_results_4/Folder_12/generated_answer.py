
def if_contains_anagrams(my_list):
    # create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # loop through each string in the list
    for string in my_list:

        # convert the string to lowercase
        # this will make the comparison case-insensitive
        string = string.lower()

        # check if the string is at least three characters long
        if len(string) < 3:
            continue


        # create a sorted version of the string
        sorted_string = "".join(sorted(string))

        # check if the sorted version of the string is already in the dictionary
        if sorted_string in anagram_pairs:

            # increment the count for this pair
            anagram_pairs[sorted_string] += 1

        else:

            # add a new entry to the dictionary with a count of one
            anagram_pairs[sorted_string] = 1

    # loop through each pair in the dictionary and check if it has more than 92 pairs
    for pair, count in anagram_pairs.items():
        if count > 92:
            return False

    # if we reach this point, then there are at most 92 pairs of anagrams in the list
    return True
