
def if_contains_anagrams(strings):
    # Count the number of anagram pairs
    pairs = 0
    
    # Loop through each string in the list
    for i in range(len(strings)):
        # Convert string to lowercase for case-insensitive comparison
        lower_string = strings[i].lower()
        
        # Check if the current string has at least length 3
        if len(lower_string) >= 3:
            # Loop through the remaining strings
            for j in range(i + 1, len(strings)):
                # Convert the other string to lowercase
                lower_other_string = strings[j].lower()
                
                # Check if the other string has at least length 3
                if len(lower_other_string) >= 3:
                    # Check if the strings are anagrams
                    if sorted(lower_string) == sorted(lower_other_string):
                        # Increment the number of anagram pairs
                        pairs += 1
                        
                        # Check if the number of pairs exceeds 69
                        if pairs > 69:
                            return False
                            
    # If the loop completes without returning False, return True
    return True
