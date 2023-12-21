
def if_contains_anagrams(lst):
    from collections import Counter
    
    count = 0
    
    # Iterate through each string in the list
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            # Convert both strings to lowercase and remove non-alphabetic characters
            str1 = ''.join(c.lower() for c in lst[i] if c.isalpha())
            str2 = ''.join(c.lower() for c in lst[j] if c.isalpha())
            
            # Check if the length of the anagram is at least three
            if len(str1) >= 3 and len(str2) >= 3:
                
                # Check if the strings are anagrams
                if Counter(str1) == Counter(str2):
                    count += 1
                    
                    # Return False if more than 25 pairs of anagrams are found
                    if count > 25:
                        return False
    
    # Return True if at most 25 pairs of anagrams are found
    return True
