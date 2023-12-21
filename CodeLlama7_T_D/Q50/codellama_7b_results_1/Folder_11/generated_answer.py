
def if_contains_anagrams(strings):
    # Initialize variables for counting anagram pairs
    pair_count = 0
    # Loop through each string in the input list
    for i in range(len(strings)):
        # Get the current string
        string1 = strings[i]
        # Loop through each subsequent string in the input list
        for j in range(i+1, len(strings)):
            # Get the current string
            string2 = strings[j]
            # Check if the two strings are anagrams of each other
            if sorted(string1) == sorted(string2):
                # If they are, increment the pair count
                pair_count += 1
                
    # Return whether there are at least 28 pairs of anagrams in the input list
    return pair_count >= 28
