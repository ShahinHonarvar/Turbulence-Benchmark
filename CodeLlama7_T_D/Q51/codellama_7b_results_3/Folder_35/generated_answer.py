
def if_contains_anagrams(word_list):
    # Create a counter for the number of anagrams in the list
    anagram_count = 0

    # Iterate over each word in the list
    for word in word_list:
        # Check if the word is an anagram of itself
        if len(word) >= 3 and sorted(word.lower()) == sorted(word):
            anagram_count += 1

    # Return true if there are at most 210 pairs of anagrams in the list, otherwise return false
    return anagram_count <= 210
