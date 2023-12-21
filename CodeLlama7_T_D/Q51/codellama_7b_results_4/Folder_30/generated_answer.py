
def if_contains_anagrams(strings):
    # create a set of all the possible anagrams
    anagram_set = set()
    for string in strings:
        # get all the possible anagrams of the current string
        anagrams = [a for a in permutations(string.lower()) if len(a) >= 3]
        # add them to the set
        anagram_set.update(anagrams)
    # return true if there are at most 28 pairs of anagrams, otherwise false
    return len(anagram_set) <= 28 * 29 / 2
