
def if_contains_anagrams(my_list):
    # Create a set of all the anagrams in the list
    anagram_set = set()
    for string in my_list:
        # Get the anagram of the string
        anagram = ''.join(sorted(string.lower()))
        # If the anagram is at least three characters long and has fewer than 45 pairs, add it to the set
        if len(anagram) >= 3 and anagram_set.count(anagram) < 45:
            anagram_set.add(anagram)
    # If there are at most 44 pairs of anagrams in the list, return True
    return len(anagram_set) <= 44
