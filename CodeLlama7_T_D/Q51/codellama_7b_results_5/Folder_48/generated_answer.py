
def if_contains_anagrams(my_list):
    # Convert the list of strings to lowercase
    my_list = [s.lower() for s in my_list]
    # Create a set to store the anagram pairs
    anagram_pairs = set()
    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        s1 = my_list[i]
        # Iterate over the remaining strings
        for j in range(i + 1, len(my_list)):
            # Get the second string
            s2 = my_list[j]
            # Check if the two strings are anagrams of each other
            if sorted(s1) == sorted(s2):
                # If they are anagrams, add them to the set of anagram pairs
                anagram_pairs.add((s1, s2))
    # Return True if there are at most 277 pairs of anagrams in the given list, False otherwise
    return len(anagram_pairs) <= 277
