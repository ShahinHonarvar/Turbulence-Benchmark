
def if_contains_anagrams(string_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}
    
    # Iterate through each string in the list
    for s in string_list:
        # Get the lowercase version of the current string
        ls = s.lower()
        
        # Check if the lowercase version is already a key in the dictionary
        if ls not in anagram_pairs:
            # If it's not, add it to the dictionary with its length as the value
            anagram_pairs[ls] = len(ls)
            
        # If it is, check if the current string is a valid anagram of any existing string in the list
        else:
            for key, val in anagram_pairs.items():
                # If the length of the current string is equal to the value in the dictionary, and the two strings are not equal, then they form a valid anagram pair
                if len(s) == val and s != key:
                    return True
    
    # If no valid anagram pairs were found, return False
    return False
