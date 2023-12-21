
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for word in my_list:
        # Check if the word has at least three characters
        if len(word) < 3:
            continue

        # Convert the word to lowercase
        word = word.lower()

        # Check if the anagram of the word is already in the dictionary
        if word in anagram_counts:
            anagram_counts[word] += 1
        else:
            # If not, add it to the dictionary with a count of 1
            anagram_counts[word] = 1

    # Check if there are at least 60 pairs of anagrams in the list
    for word, count in anagram_counts.items():
        if count >= 60:
            return True

    return False
