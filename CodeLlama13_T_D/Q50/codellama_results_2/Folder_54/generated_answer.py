
def if_contains_anagrams(str_list):
    # Initialize a dictionary to store the count of anagrams for each string length
    anagram_counts = {}
    
    # Iterate over the list of strings and check if any two strings are anagrams
    for str1 in str_list:
        for str2 in str_list[str_list.index(str1) + 1:]:
            # Check if the two strings have the same length and case-insensitive match
            if len(str1) >= 3 and len(str2) >= 3 and str1.lower() == str2.lower():
                # If they are anagrams, increment the count for their length by 1
                anagram_counts[len(str1)] = anagram_counts.get(len(str1), 0) + 1
    
    # Return true if there are at least 74 pairs of anagrams in the list, otherwise false
    return len([x for x in anagram_counts.values() if x >= 2]) >= 74
