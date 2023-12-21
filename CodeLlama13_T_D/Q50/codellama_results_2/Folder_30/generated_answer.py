
def if_contains_anagrams(strings):
    # Initialize an empty dictionary to store the counts of anagrams
    anagram_counts = {}
    
    # Iterate over the list of strings and increment the count for each anagram in the dictionary
    for string in strings:
        if len(string) >= 3:
            sorted_string = "".join(sorted(string.lower()))
            if sorted_string not in anagram_counts:
                anagram_counts[sorted_string] = 1
            else:
                anagram_counts[sorted_string] += 1
    
    # Check if there are at least 78 pairs of anagrams in the dictionary
    return len(anagram_counts) >= 78
