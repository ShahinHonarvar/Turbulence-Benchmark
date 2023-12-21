
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts for each string
    anagram_counts = {}
    
    # Loop through each string in the list
    for string in strings:
        # Get the lowercase version of the string and remove duplicates
        lowercase_string = "".join(sorted(set(string.lower())))
        
        # If the string is at least three characters long, add it to the dictionary
        if len(lowercase_string) >= 3:
            anagram_counts[lowercase_string] = anagram_counts.get(lowercase_string, 0) + 1
    
    # Check if there are at most 96 pairs of anagrams in the list
    return len([key for key, value in anagram_counts.items() if value > 1]) <= 96
