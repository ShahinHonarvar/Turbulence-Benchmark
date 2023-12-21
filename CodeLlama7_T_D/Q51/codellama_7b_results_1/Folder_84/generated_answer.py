
def if_contains_anagrams(my_list):
    # Create a set of all anagram possibilities
    anagram_possibilities = set()
    for word in my_list:
        # Ignore words that are not at least three letters long
        if len(word) < 3:
            continue

        # Generate all possible anagrams of the word
        anagrams = []
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                anagrams.append("".join(sorted(word[i:j]))))
        # Add all generated anagrams to the set of possibilities
        for anagram in anagrams:
            if anagram in anagram_possibilities:
                continue

            else:

                anagram_possibilities.add(anagram)
    # Return True if there are at most 16 pairs of anagrams in the given list, otherwise return False
    if len(anagram_possibilities) > 16:
        return False

    else:

        return True
