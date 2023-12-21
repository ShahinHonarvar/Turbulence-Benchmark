
def if_contains_anagrams(my_list):
    # Initialize a set to store the anagrams
    anagrams = set()
    
    # Iterate through the list of strings
    for word in my_list:
        # Convert the current string to lowercase
        lowercase_word = word.lower()
        
        # Sort the characters in the current string
        sorted_chars = "".join(sorted(lowercase_word))
        
        # If the sorted string is not already in the set, add it to the set
        if sorted_chars not in anagrams:
            anagrams.add(sorted_chars)
    
    # Check if there are at least 59 pairs of anagrams in the set
    return len(anagrams) >= 59
