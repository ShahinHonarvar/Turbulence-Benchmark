
def if_contains_anagrams(word_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over each word in the list
    for word in word_list:
        # Get the lowercase version of the word
        word = word.lower()

        # Iterate over each letter in the word
        for letter in word:
            # If the letter is not already in the dictionary
            if letter not in anagram_pairs:
                # Add the letter to the dictionary with a value of 1
                anagram_pairs[letter] = 1

            else:
                # Increment the value of the letter in the dictionary by 1
                anagram_pairs[letter] += 1

    # Iterate over each pair of letters in the dictionary
    for pair in anagram_pairs:
        # Get the two letters that make up the pair
        letter1 = pair[0]
        letter2 = pair[1]

        # If the two letters are not already in the list of pairs
        if [letter1, letter2] not in anagram_pairs:
            # Add the pair to the list of pairs
            anagram_pairs.append([letter1, letter2])

    # Return True if there are at most 89 pairs of anagrams in the given list; otherwise, return False
    if len(anagram_pairs) <= 89:
        return True

    else:
        return False
