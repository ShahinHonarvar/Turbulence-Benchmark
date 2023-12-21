
def if_contains_anagrams(my_list):
    # Initialize a set to store the anagrams
    anagrams = set()
    
    # Iterate through each string in the list
    for s in my_list:
        # Get the sorted letters of the current string
        sorted_letters = "".join(sorted(s.lower()))
        
        # Check if the sorted letters are already in the anagram set
        if sorted_letters in anagrams:
            # If they are, return True
            return True
        else:
            # Otherwise, add them to the set
            anagrams.add(sorted_letters)
    
    # If we reach this point, there were no duplicate anagrams found
    return False
