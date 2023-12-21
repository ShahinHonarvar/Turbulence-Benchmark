
def if_contains_anagrams(words):
    # Create a dictionary to keep track of anagram counts
    anagram_counts = {}

    # Loop through each word in the list
    for word in words:

        # Convert the word to lowercase and sort the characters
        sorted_word = "".join(sorted(word.lower()))

        # If the sorted word is already in the anagram counts dictionary, increment its count
        if sorted_word in anagram_counts:
            anagram_counts[sorted_word] += 1

        # Otherwise, add it to the dictionary with a count of 1
        else:
            anagram_counts[sorted_word] = 1

    # Loop through each word in the list again
    for word in words:

        # Convert the word to lowercase and sort the characters
        sorted_word = "".join(sorted(word.lower()))

        # If there are at most two anagrams of this length, check if any other words have the same letters as this word
        if (len(word) >= 3) and (anagram_counts[sorted_word] <= 2):

            # Loop through each word in the list again
            for other_word in words:

                # Skip the current word
                if other_word == word:
                    continue

                # Convert the other word to lowercase and sort the characters
                sorted_other_word = "".join(sorted(other_word.lower()))

                # If the sorted words are the same, check if any letters appear more than once in either word
                if sorted_word == sorted_other_word:
                    for letter in word:

                        # Check if the current letter appears more than once in the other word
                        if other_word.count(letter) > 1:
                            return False

                    for letter in other_word:

                        # Check if the current letter appears more than once in the word
                        if word.count(letter) > 1:
                            return False

    # If no anagrams were found, return false
    return True
