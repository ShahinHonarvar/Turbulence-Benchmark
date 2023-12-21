
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_length = 0
    
    # Iterate through the list of strings
    for string1 in my_list:
        # Skip over short strings (<3 characters)
        if len(string1) < 3:
            continue
        
        # Check for anagrams by comparing each string to its reversed version
        for string2 in my_list:
            # Ignore the original string and any duplicates
            if string1 == string2 or string1 in [string2, string2]:
                continue
            
            # If the strings are anagrams, increase the count
            if sorted(string1) == sorted(string2):
                anagram_count += 1
                break
        
        # Update the count for each three-or-more character string
        if len(string1) >= 3:
            three_or_more_length += 1
    
    # Return true if there are at least 14 pairs of anagrams, false otherwise
    return anagram_count >= 14 and three_or_more_length >= 14
