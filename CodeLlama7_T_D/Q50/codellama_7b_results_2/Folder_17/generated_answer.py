
def if_contains_anagrams(my_list):
    # check length of list and return False if it's less than 97
    if len(my_list) < 97:
        return False

    # create a dictionary to store the anagram counts

    anagram_counts = {}

    # loop through each string in the list

    for string in my_list:

        # convert the string to lowercase

        string = string.lower()

        # sort the characters in the string

        sorted_chars = ''.join(sorted(string))

        # check if the sorted string is already in the dictionary

        if sorted_chars in anagram_counts:

            # increment the count for this anagram

            anagram_counts[sorted_chars] += 1

        else:

            # add a new entry to the dictionary with a count of 1

            anagram_counts[sorted_chars] = 1

    # loop through each anagram in the dictionary

    for sorted_string, count in anagram_counts.items():

        # check if the count is at least 3 and return True

        if count >= 3:

            return True
