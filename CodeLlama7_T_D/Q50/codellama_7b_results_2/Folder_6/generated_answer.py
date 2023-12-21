
def if_contains_anagrams(words):
    # Initialize a counter for the number of anagram pairs
    pair_count = 0

    # Iterate over each word in the list
    for i in range(len(words)):
        # Get the current word
        word1 = words[i]

        # Check if the current word has at least three letters
        if len(word1) >= 3:
            # Convert the current word to lowercase
            word1_lower = word1.lower()

            # Iterate over each subsequent word in the list
            for j in range(i + 1, len(words)):
                # Get the next word
                word2 = words[j]

                # Check if the next word has at least three letters and is not the current word
                if len(word2) >= 3 and word2 != word1:
                    # Convert the next word to lowercase
                    word2_lower = word2.lower()

                    # Check if the current word and the next word are anagrams of each other
                    if sorted(word1_lower) == sorted(word2_lower):
                        # Increment the pair counter
                        pair_count += 1

                        # If there are at least 26 pairs, return True
                        if pair_count >= 26:
                            return True

    # If there are less than 26 pairs, return False
    return False
