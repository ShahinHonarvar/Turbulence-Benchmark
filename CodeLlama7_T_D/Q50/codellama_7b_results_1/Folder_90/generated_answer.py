
def if_contains_anagrams(word_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for word in word_list:
        # Check if the word has at least three letters
        if len(word) < 3:
            continue

        # Convert the word to lowercase
        word = word.lower()

        # Create an anagram of the word by rearranging its letters
        for i in range(len(word)):
            for j in range(i+1, len(word))):
                anagram = word[i] + word[j] + word[i+1:j] + word[j+1:]
                # Check if the anagram is already in the dictionary
                if anagram not in anagram_counts:
                    anagram_counts[anagram] = 1

                else:
                    anagram_counts[anagram] += 1

        # Check if there are at least 177 pairs of anagrams in the dictionary
        if len(anagram_counts) >= 177:
            return True

    # If no anagram pair was found, return False
    return False
