
def if_contains_anagrams(words):
    # Create a set of all letters in the alphabet (ignoring case)
    all_letters = set('abcdefghijklmnopqrstuvwxyz')
    # Initialize variables to keep track of anagram pairs and length of words
    pair_count = 0
    word_length = 0
    # Iterate over the list of words
    for word in words:
        # Convert the word to lowercase
        word = word.lower()
        # Check if the word is at least three letters long
        if len(word) < 3:
            continue

        # Create a set of all letters in the word (ignoring case)
        letter_set = set(word)
        # Check if the word contains any anagrams
        for other_word in words:
            # Convert the other word to lowercase
            other_word = other_word.lower()
            # Check if the other word is at least three letters long
            if len(other_word) < 3:
                continue

            # Create a set of all letters in the other word (ignoring case)
            other_letter_set = set(other_word)
            # Check if the other word contains any anagrams
            if letter_set == other_letter_set:
                # If the words are anagrams, increase the pair count and break out of the inner loop
                pair_count += 1
                break

        # If there are at most 401 pairs of anagrams in the given list, return True
        if pair_count <= 401:
            return True

    # Otherwise, return False
    else:
        return False
