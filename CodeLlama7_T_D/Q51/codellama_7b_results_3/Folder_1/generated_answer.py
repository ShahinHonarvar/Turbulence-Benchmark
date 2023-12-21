
def if_contains_anagrams(words):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over each word in the list
    for word in words:
        # Convert the word to lowercase
        word = word.lower()

        # Check if the word is at least three characters long
        if len(word) < 3:
            continue

        # Create a tuple of the anagrammed letters
        anagram_tuple = tuple(sorted(word))

        # Increment the count for this anagram
        anagram_counts[anagram_tuple] = anagram_counts.get(anagram_tuple, 0) + 1

    # Check if there are at most 30 pairs of anagrams in the list
    return len(anagram_counts) <= 30
