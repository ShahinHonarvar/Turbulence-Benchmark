
def if_contains_anagrams(word_list):
    # Get the number of words in the list
    num_words = len(word_list)
    # Initialize a counter for the number of anagram pairs
    num_anagram_pairs = 0
    # Iterate over each word in the list
    for i in range(num_words):
        # Get the current word
        word1 = word_list[i]
        # Iterate over each other word in the list
        for j in range(num_words):
            # Get the second word
            word2 = word_list[j]
            # Check if the two words are anagrams of each other
            if sorted(word1) == sorted(word2):
                # Increment the number of anagram pairs
                num_anagram_pairs += 1
    # Return True if there are at least 75 anagram pairs in the list, and False otherwise
    return num_anagram_pairs >= 75
