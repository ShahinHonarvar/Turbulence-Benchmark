
def if_contains_anagrams(my_list):
    # Get the length of the list
    n = len(my_list)
    # Initialize a counter for pairs of anagrams
    pair_count = 0

    # Iterate over each string in the list
    for i in range(n):
        # Get the current string
        s1 = my_list[i]
        # Iterate over each other string in the list
        for j in range(i+1, n):
            # Get the other string
            s2 = my_list[j]
            # Check if the strings are anagrams
            if sorted(s1.lower()) == sorted(s2.lower()):
                # Increment the pair counter
                pair_count += 1

    # Return True if there are at least 68 pairs of anagrams, otherwise False
    return pair_count >= 68
