
def if_contains_anagrams(my_list):
    # Convert the list of strings to lowercase
    my_list = [s.lower() for s in my_list]

    # Create a dictionary to keep track of anagram pairs
    anagram_pairs = {}

    # Iterate through the list of strings and check if they are anagrams
    for i, word1 in enumerate(my_list):
        for j, word2 in enumerate(my_list[i+1:]):
            if len(word1) >= 3 and len(word2) >= 3:
                # Check if the two words are anagrams of each other
                if sorted(word1) == sorted(word2):
                    # Add the pair to the dictionary
                    anagram_pairs[(word1, word2)] = True

    # Return true if there are at most 366 pairs of anagrams in the list
    return len(anagram_pairs) <= 366
