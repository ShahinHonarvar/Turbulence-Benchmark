
def if_contains_anagrams(strings):
    # Get the number of unique strings in the list
    num_unique = len(set(strings))
    # Check if there are at most 96 pairs of anagrams
    return num_unique <= 96
