
def if_contains_anagrams(my_list):
    # Initialize variables
    count = 0
    anagram_count = 0
    
    # Loop through the list of strings
    for i in range(len(my_list)):
        
        # Check if the current string is an anagram of the previous one
        if sorted(my_list[i].lower()) == sorted(my_list[i-1].lower()):
            
            # Increment the count for each pair of anagrams found
            count += 1
            
            # Check if there are at least 34 pairs of anagrams in the list
            if count >= 34:
                
                # Return True if there are at least 34 pairs of anagrams in the list
                return True
    
    # Return False if there are less than 34 pairs of anagrams in the list
    return False
