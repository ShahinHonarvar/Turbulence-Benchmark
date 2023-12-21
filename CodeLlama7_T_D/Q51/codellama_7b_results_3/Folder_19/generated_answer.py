
def if_contains_anagrams(str_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the list of strings
    for str1 in str_list:
        # Convert the string to lowercase
        str1_lower = str1.lower()
        # Iterate over the rest of the list of strings
        for str2 in str_list[str_list.index(str1) + 1 : ]:
            # Convert the string to lowercase
            str2_lower = str2.lower()
            # Check if the two strings are anagrams
            if sorted(str1_lower) == sorted(str2_lower):
                # If they are, add them to the dictionary of anagram pairs
                anagram_pairs[(str1_lower, str2_lower)] = 0

    # Check if there are more than 69 pairs of anagrams in the list
    return len(anagram_pairs) <= 69
