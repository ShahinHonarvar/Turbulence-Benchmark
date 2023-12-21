
def if_contains_anagrams(strings):
    # Initialize a set to store the anagrams
    anagrams = set()
    
    # Iterate over the list of strings
    for string in strings:
        # Convert the string to lowercase and sort its characters
        sorted_chars = "".join(sorted(string.lower()))
        
        # If the sorted characters are already in the anagram set, return False
        if sorted_chars in anagrams:
            return False
        
        # Add the sorted characters to the anagram set
        anagrams.add(sorted_chars)
    
    # If the anagram set has at most 98 pairs, return True
    return len(anagrams) <= 98
