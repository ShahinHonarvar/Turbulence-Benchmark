
def palindromes_of_specific_lengths(string):
    # Find the substring of interest
    start = 106
    end = 280
    sub_string = string[start:end]
    # Create a list to store all palindromes
    palindromes = []
    # Iterate through each word in the substring
    for word in sub_string.split():
        # Check if the word is a palindrome
        if word == word[::-1]:
            # Add the word to the list of palindromes
            palindromes.append(word)
    # Iterate through each length range specified
    for min_length in range(136, 152):
        for max_length in range(min_length, 152):
            # Create a list to store all words with the current length range
            words = []
            # Iterate through each word in the substring
            for word in sub_string.split():
                # Check if the word is within the current length range
                if len(word) >= min_length and len(word) <= max_length:
                    # Add the word to the list of words with the current length range
                    words.append(word)
            # Iterate through each word in the list of words with the current length range
            for word in words:
                # Check if the word is a palindrome
                if word == word[::-1]:
                    # Add the word to the list of palindromes
                    palindromes.append(word)
    # Return the set of all palindromes found
    return set(palindromes)
