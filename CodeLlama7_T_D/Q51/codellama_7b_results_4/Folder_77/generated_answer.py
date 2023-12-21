
def if_contains_anagrams(strings):
    # Set of all possible anagram pairs
    anagram_pairs = set()
    for string in strings:
        # Convert string to lowercase
        string = string.lower()
        # Generate all possible anagram pairs
        for i in range(len(string) - 1):
            for j in range(i + 1, len(string))):
                # Add the anagram pair to the set
                anagram_pairs.add((string[i], string[j])))
    # Return true if there are at most 17 pairs of anagrams in the given list
    return len(anagram_pairs) <= 17
