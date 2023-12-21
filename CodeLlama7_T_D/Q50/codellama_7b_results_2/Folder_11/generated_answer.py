
def if_contains_anagrams(str_list):
    # Check if the list is empty
    if len(str_list) == 0:
        return False

    # Initialize a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the strings in the list
    for str1 in str_list:

        # Check if the string is at least three characters long
        if len(str1) < 3:
            continue


        # Convert the string to lowercase
        str1 = str1.lower()

        # Iterate over the other strings in the list
        for str2 in str_list:

            # Check if the current string is not the same as the previous one
            if str1 != str2:

                # Convert the second string to lowercase
                str2 = str2.lower()

                # Check if the two strings are anagrams of each other
                if sorted(str1) == sorted(str2):

                    # Increment the count for the current anagram pair
                    if (str1, str2) in anagram_pairs:
                        anagram_pairs[(str1, str2)] += 1

                    else:

                        anagram_pairs[(str1, str2)] = 1


    # Check if there are at least 28 pairs of anagrams in the list
    return len(anagram_pairs) >= 28
