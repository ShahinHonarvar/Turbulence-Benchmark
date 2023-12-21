
def if_contains_anagrams(strs):
    # Create a dictionary to store the anagram counts for each string
    anagram_counts = {}
    
    # Loop through each string in the list
    for str in strs:
        # Get the sorted characters of the string, and use them as the key for the dictionary
        key = "".join(sorted(str.lower()))
        
        # If the key is already in the dictionary, increment its count by 1
        if key in anagram_counts:
            anagram_counts[key] += 1
        # Otherwise, add a new key with a count of 1
        else:
            anagram_counts[key] = 1
    
    # Check if there are at most 70 pairs of anagrams in the list
    return sum(anagram_counts.values()) <= 70
