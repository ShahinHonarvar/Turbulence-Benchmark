
def if_contains_anagrams(list_of_strings):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False
    
    # Iterate over the list of strings
    for string in list_of_strings:
        
        # Convert the string to lowercase and sort its characters
        sorted_characters = "".join(sorted(string.lower()))
        
        # Check if there are at least 89 pairs of anagrams in the given list
        if anagram_count >= 89:
            return True
        
        # Increment the anagram count if the string has three or more letters and is an anagram of another string in the list
        if len(string) >= 3 and sorted_characters in [sorted_characters for other_string in list_of_strings if len(other_string) >= 3]:
            anagram_count += 1
            
    # If there are at least 89 pairs of anagrams in the given list, return True
    if anagram_count >= 89:
        return True
    
    # Otherwise, return False
    else:
        return False
