
def if_contains_anagrams(word_list):
    # Define the set of all English letters
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    # Initialize a counter for the number of anagrams
    num_anagrams = 0
    # Iterate over the words in the list
    for word in word_list:
        # Check if the word is at least three letters long
        if len(word) >= 3:
            # Create a set of all the letters in the word
            letter_set = set(word.lower())
            # Check if the set of letters contains only English letters
            if letter_set <= english_letters:
                # Increment the counter for the number of anagrams
                num_anagrams += 1
    # Return True if there are at most 75 pairs of anagrams in the list, otherwise return False
    return num_anagrams <= 75
