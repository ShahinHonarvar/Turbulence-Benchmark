
def if_contains_anagrams(strings):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(strings) - 1):
        for j in range(i + 1, len(strings)):
            # If the strings are anagrams of each other...
            if sorted(strings[i]) == sorted(strings[j]):
                # Increment the number of anagram pairs
                anagram_pairs += 1
    # Return true if there are at least 49 pairs of anagrams in the list, or false otherwise
    return anagram_pairs >= 49
