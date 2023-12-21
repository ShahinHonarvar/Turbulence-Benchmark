
def if_contains_anagrams(words):
    # Create a dictionary to store the counts of each letter
    letter_counts = {}

    # Loop through each word in the list
    for word in words:
        # Convert the word to lowercase
        word = word.lower()

        # Loop through each letter in the word
        for letter in word:
            # If the letter is not already in the dictionary, add it with a count of 1
            if letter not in letter_counts:
                letter_counts[letter] = 1

            # Otherwise, increment the count of the letter
            else:
                letter_counts[letter] += 1

    # Create a list to store the anagrams
    anagrams = []

    # Loop through each word in the list
    for word in words:
        # Convert the word to lowercase
        word = word.lower()

        # If the word is not already in the list of anagrams, add it
        if word not in anagrams:
            anagrams.append(word)

    # Loop through each pair of anagrams in the list
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams))):
            # If there are at most 55 pairs of anagrams in the given list, return true
            if len(anagrams[i]) == len(anagrams[j])) and (len(anagrams[i]) >= 3)):
                return True

    # Otherwise, return false
    return False
