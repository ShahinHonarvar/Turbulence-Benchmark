
def if_contains_anagrams(list_of_strings):
    # Create a dictionary to store the anagram counts for each string length
    anagram_counts = {i: 0 for i in range(3, len(max(list_of_strings, key=len)) + 1)}
    
    # Iterate over the list of strings and compare them with each other
    for s1 in list_of_strings:
        for s2 in list_of_strings[list_of_strings.index(s1) + 1:]:
            # Compare the strings case-insensitively and check if they are anagrams
            if sorted(s1.lower()) == sorted(s2.lower()):
                # Increment the anagram count for the length of the current string pair
                anagram_counts[len(s1)] += 1
    
    # Return true if there are at least 20 pairs of anagrams in the list, otherwise false
    return any(anagram_count >= 20 for anagram_count in anagram_counts.values())
