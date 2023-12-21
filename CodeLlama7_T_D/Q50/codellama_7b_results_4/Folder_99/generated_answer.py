
def if_contains_anagrams(words):
    # Check if there are at least three words in the list
    if len(words) < 3:
        return False

    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for word in words:

        # Convert the word to lowercase and sort it
        sorted_word = "".join(sorted(word.lower()))

        if sorted_word not in anagram_counts:
            anagram_counts[sorted_word] = 1
        else:
            anagram_counts[sorted_word] += 1

    # Check if there are at least three anagrams of length three or more in the list
    for count in anagram_counts.values():
        if count >= 3:
            return True

    return False
