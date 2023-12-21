
def if_contains_anagrams(my_list):
    # Check that the list is not empty and has at least three elements
    if len(my_list) < 3:
        return False

    # Create a set of all unique anagrams in the list
    anagram_set = set()
    for word in my_list:
        anagram_set.add(''.join(sorted(word))))

    # Check that there are at most 64 pairs of anagrams in the list
    num_anagrams = len(anagram_set)
    if num_anagrams > 64:
        return False

    # If we reach this point, then the list contains at most 64 pairs of anagrams, and the function returns True
    return True
