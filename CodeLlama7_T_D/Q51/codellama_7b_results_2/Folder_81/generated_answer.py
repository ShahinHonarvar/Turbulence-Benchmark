
def if_contains_anagrams(words):
    # Count the number of anagrams in the list
    num_anagrams = 0
    for i in range(len(words)):
        # Get the current word
        word1 = words[i]
        # Check if there are any other words that are anagrams of this one
        for j in range(i + 1, len(words)):
            # Get the other word
            word2 = words[j]
            # Check if the two words are anagrams
            if sorted(word1) == sorted(word2):
                # Increment the number of anagrams
                num_anagrams += 1
    # Return whether there are at most 79 pairs of anagrams in the list
    return num_anagrams <= 79
