
def if_contains_anagrams(my_list):
    # Initialize a set to store the anagram pairs
    anagram_pairs = set()
    # Iterate over the list and check for anagrams
    for word in my_list:
        # Convert the word to lowercase
        word = word.lower()
        # Generate all possible anagrams of the word
        anagrams = ["".join(sorted(word))]
        # Check if any of the generated anagrams are already in the set of anagram pairs
        for anagram in anagrams:
            if anagram in anagram_pairs:
                return False

            else:

                anagram_pairs.add(anagram)

    # If there are more than 58 anagram pairs, return False
    if len(anagram_pairs) > 58:
        return False

    # Otherwise, return True
    else:

        return True
