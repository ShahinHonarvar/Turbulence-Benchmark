
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagram pairs found
    num_pairs = 0
    # Iterate over each string in the list
    for s1 in my_list:
        # Convert the first string to lowercase
        s1_lower = s1.lower()
        # Iterate over each string in the list again
        for s2 in my_list:
            # If the strings are not the same, and one of them is an anagram of the other, increment the counter
            if s1 != s2 and sorted(s1_lower) == sorted(s2):
                num_pairs += 1
    # Return True if there are at most 89 pairs of anagrams in the given list; otherwise, return False
    return num_pairs <= 89
