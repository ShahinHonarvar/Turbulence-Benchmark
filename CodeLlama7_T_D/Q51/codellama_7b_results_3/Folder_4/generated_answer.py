
def if_contains_anagrams(my_list):
    # Create a set to keep track of anagram pairs
    anagram_pairs = set()
    # Iterate over the list of strings
    for string1 in my_list:
        # Convert the string to lowercase
        string1_lowercase = string1.lower()
        # Sort the characters in the string
        sorted_string1 = "".join(sorted(string1_lowercase))
        # Iterate over the list of strings again
        for string2 in my_list:
            # Convert the string to lowercase
            string2_lowercase = string2.lower()
            # Sort the characters in the string
            sorted_string2 = "".join(sorted(string2_lowercase))
            # If the strings are anagrams of each other, add them to the set of anagram pairs
            if sorted_string1 == sorted_string2:
                anagram_pairs.add((string1, string2))
    # Return True if there are at most 84 pairs of anagrams in the list; otherwise, return False
    return len(anagram_pairs) <= 84
