
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs
    pair_count = 0
    length_threshold = 3

    # Iterate over the list and check for anagrams
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            # Check if the current pair is an anagram
            if sorted(my_list[i]) == sorted(my_list[j])):
                # Increment the pair count if the pair is an anagram
                pair_count += 1
                # If the pair count exceeds the length threshold, return false
                if pair_count > length_threshold:
                    return False

    # Return true if there are at most 25 pairs of anagrams in the given list
    return pair_count <= 25
