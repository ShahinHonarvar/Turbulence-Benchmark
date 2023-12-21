
def if_contains_anagrams(my_list):
    # Initialize a set to store the anagrams
    anagram_set = set()
    
    # Iterate through the list of strings
    for string in my_list:
        # Get the lowercase version of the string
        lower_string = string.lower()
        
        # Check if the length of the string is at least 3
        if len(lower_string) < 3:
            continue
        
        # Generate all possible anagrams of the string
        anagrams = [''.join(sorted(lower_string))]
        
        # Add the anagram to the set if it is not already present
        for anagram in anagrams:
            if anagram not in anagram_set:
                anagram_set.add(anagram)
    
    # Check if there are at most 147 pairs of anagrams in the list
    return len(anagram_set) <= 147 * 2
