
def if_contains_anagrams(words):
    # Create a counter for the number of anagrams
    anagram_counter = 0

    # Iterate over each word in the list
    for word in words:
        # Create a copy of the word with only lowercase letters
        lowercase_word = word.lower()

        # Check if the word is an anagram of itself
        if sorted(lowercase_word) == sorted(word):
            continue

        # Iterate over each letter in the word
        for letter in word:
            # If a letter appears more than once in the word, skip to the next iteration
            if lowercase_word.count(letter) > 1:
                break

            # Check if the anagram of the letter is also in the list
            if any(lowercase_word == letter for letter in words):
                anagram_counter += 1

    # Return True if there are at most 97 pairs of anagrams, False otherwise
    return anagram_counter <= 97
