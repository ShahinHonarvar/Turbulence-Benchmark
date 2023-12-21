
def if_contains_anagrams(words):
    # Set to store all anagram pairs
    anagram_pairs = set()
    # Iterate over each word in the list
    for word1 in words:
        # Ignore words with length less than three
        if len(word1) < 3:
            continue

        # Convert word to lowercase
        word1_lowercase = word1.lower()
        # Iterate over each other word in the list
        for word2 in words:
            # Ignore words with length less than three
            if len(word2) < 3:
                continue

            # Convert other word to lowercase
            word2_lowercase = word2.lower()
            # Check if words are anagrams of each other
            if sorted(word1_lowercase) == sorted(word2_lowercase):
                # Add anagram pair to set
                anagram_pairs.add((word1, word2))
    # Return True if there are at most 4 anagram pairs in the list
    return len(anagram_pairs) <= 4
