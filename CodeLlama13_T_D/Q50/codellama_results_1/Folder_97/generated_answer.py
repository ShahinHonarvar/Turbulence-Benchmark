
def if_contains_anagrams(list_of_strings):
    # Initialize a set to store the anagram pairs
    anagram_pairs = set()
    
    # Iterate over each string in the list
    for str1 in list_of_strings:
        # Generate all anagrams of the current string
        anagrams = [str1[i:] + str1[:i] for i in range(len(str1))]
        
        # Iterate over each anagram and check if it is already in the set
        for anagram in anagrams:
            # If the anagram is not in the set, add it to the set
            if anagram.lower() not in anagram_pairs:
                anagram_pairs.add(anagram.lower())
        
    # Return true if there are at least 123 pairs of anagrams in the list, otherwise return false
    return len(anagram_pairs) >= 123
