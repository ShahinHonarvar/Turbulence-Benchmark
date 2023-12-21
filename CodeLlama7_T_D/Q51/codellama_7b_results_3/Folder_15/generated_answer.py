
def if_contains_anagrams(words):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    for word in words:
        # Get the anagram of the word
        anagram = ''.join(sorted(word.lower()))

        if len(anagram) < 3:
            # If the anagram is shorter than three characters, ignore it
            continue

        if anagram in anagram_counts:
            # If the anagram has already been seen before, increment its count
            anagram_counts[anagram] += 1

        else:
            # If this is a new anagram, add it to the dictionary with a count of one
            anagram_counts[anagram] = 1

    # Check if there are at most 20 pairs of anagrams in the list
    return len(anagram_counts) <= 20
