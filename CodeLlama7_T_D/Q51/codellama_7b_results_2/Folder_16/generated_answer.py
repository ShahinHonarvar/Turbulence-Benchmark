
def if_contains_anagrams(str_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over each string in the list
    for str1 in str_list:

        # Convert both strings to lowercase
        str1 = str1.lower()

        # Iterate over each string in the list again
        for str2 in str_list:

            # If the current string is not the same as the previous string
            if str1 != str2:

                # Convert both strings to lowercase
                str2 = str2.lower()

                # Check if the two strings are anagrams of each other
                if sorted(str1) == sorted(str2):

                    # If the current string is not in the dictionary, add it as a key with an empty list as its value
                    if str1 not in anagram_pairs:
                        anagram_pairs[str1] = []

                    # Add the other string as a value to the corresponding key in the dictionary
                    anagram_pairs[str1].append(str2)

    # Return False if there are more than 24 pairs of anagrams in the list
    return len(anagram_pairs) <= 24
