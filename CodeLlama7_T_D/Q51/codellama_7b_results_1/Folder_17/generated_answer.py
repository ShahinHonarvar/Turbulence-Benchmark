
def if_contains_anagrams(words):
    # Create a dictionary to keep track of anagram pairs
    anagram_pairs = {}
    # Loop through each word in the list
    for word in words:
        # Convert the word to lowercase
        lowercase_word = word.lower()
        # Check if there are any anagrams of this word
        if len(lowercase_word) > 2:
            # If there are, loop through each one and check if it's already been seen
            for i in range(len(lowercase_word)):
                for j in range(i+1, len(lowercase_word)):
                    anagram = ''.join(sorted(lowercase_word[i] + lowercase_word[j])))
                    if anagram in anagram_pairs:
                        # If the anagram has already been seen, increase the count by 1
                        anagram_pairs[anagram] += 1
                    else:
                        # If this is a new anagram, add it to the dictionary with a count of 1
                        anagram_pairs[anagram] = 1
            # Check if there are at most 22 pairs of anagrams in the list
            if len(anagram_pairs) > 22:
                return False
    # If all anagrams have been checked and there are no more than 22 pairs, return True
    return True
