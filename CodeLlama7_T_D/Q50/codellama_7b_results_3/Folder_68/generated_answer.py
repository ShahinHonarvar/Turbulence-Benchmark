
def if_contains_anagrams(str_list):
    # Initialize the dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the list of strings
    for str1 in str_list:
        # Convert both strings to lowercase
        str1_lower = str1.lower()

        # Iterate over the remaining strings
        for str2 in str_list[str_list.index(str1) + 1:]:
            # Convert both strings to lowercase
            str2_lower = str2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(str1_lower) == sorted(str2_lower):
                # If the two strings are anagrams, add them to the dictionary
                if (str1_lower, str2_lower) not in anagram_pairs:
                    anagram_pairs[(str1_lower, str2_lower)] = 1
                else:
                    # If the two strings are already in the dictionary, increment their count by one
                    anagram_pairs[(str1_lower, str2_lower)] += 1

        # Check if there are at least 9 pairs of anagrams in the given list
        if len(anagram_pairs) >= 9:
            return True

    # If there are not at least 9 pairs of anagrams in the given list, return false
    else:
        return False
