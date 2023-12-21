
def if_contains_anagrams(words):
    # Create a dictionary to keep track of anagram pairs
    anagram_pairs = {}

    for word1 in words:
        # Convert word1 to lowercase and remove spaces
        word1_lower = word1.lower().replace(" ", "")

        for word2 in words:
            # Convert word2 to lowercase and remove spaces
            word2_lower = word2.lower().replace(" ", "")

            if word1_lower != word2_lower:
                # Check if the two words are anagrams of each other
                if sorted(word1_lower) == sorted(word2_lower):
                    # If so, add them to the dictionary of anagram pairs
                    if (word1_lower, word2_lower) in anagram_pairs:
                        anagram_pairs[(word1_lower, word2_lower)] += 1

                    else:
                        anagram_pairs[(word1_lower, word2_lower)] = 1

    # Check if there are more than 392 pairs of anagrams in the given list
    if len(anagram_pairs) > 392:
        return False

    else:
        return True
