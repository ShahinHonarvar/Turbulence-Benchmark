
def if_contains_anagrams(word_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}
    # Iterate over the words in the list
    for word1 in word_list:
        # Check if the word is at least three characters long
        if len(word1) >= 3:
            # Convert the word to lowercase
            word1_lower = word1.lower()
            # Iterate over the words in the list again
            for word2 in word_list:
                # Check if the word is at least three characters long
                if len(word2) >= 3:
                    # Convert the word to lowercase
                    word2_lower = word2.lower()
                    # Check if the words are not the same and have the same length
                    if word1_lower != word2_lower and len(word1_lower) == len(word2_lower):
                        # Check if the words are anagrams of each other
                        if sorted(word1_lower) == sorted(word2_lower):
                            # If the words are anagrams, add them to the dictionary
                            anagram_pairs[word1_lower] = word2_lower
    # Check if there are at most 74 pairs of anagrams in the list
    return len(anagram_pairs) <= 74
