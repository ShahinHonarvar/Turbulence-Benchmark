
def if_contains_anagrams(my_list):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(my_list) - 1):
        # Get the current string and the next string in the list
        s1 = my_list[i]
        s2 = my_list[i + 1]
        # Check if the two strings are anagrams of each other
        if sorted(s1) == sorted(s2):
            # If they are, increment the number of anagram pairs
            anagram_pairs += 1
    # Return True if there are at most 91 pairs of anagrams in the list; otherwise, return False.
    return anagram_pairs <= 91
