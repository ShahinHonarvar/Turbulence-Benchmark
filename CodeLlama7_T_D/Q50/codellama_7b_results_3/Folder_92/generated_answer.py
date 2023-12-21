
def if_contains_anagrams(my_list):
    # Create a set to store all anagrams
    anagrams = set()
    # Iterate over the list and check for anagrams
    for word in my_list:
        # Get the anagram of the current word
        anagram = ''.join(sorted(word))
        # If the anagram is already in the set, return True
        if anagram in anagrams:
            return True

        # Add the anagram to the set
        anagrams.add(anagram)
    # If no anagrams were found, return False
    return False
