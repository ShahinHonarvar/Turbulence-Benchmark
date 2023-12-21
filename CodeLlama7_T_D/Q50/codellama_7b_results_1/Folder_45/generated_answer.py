
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs
    pair_count = 0
    three_letter_count = 0

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]
        # Check if the current string is an anagram of another string in the list
        for j in range(len(my_list)):
            # Skip the current string and its corresponding anagram pair
            if i == j:
                continue

            # Get the second string
            second_str = my_list[j]
            # Check if the two strings are anagrams of each other
            if sorted(curr_str) == sorted(second_str):
                # Increment the pair count if the current string is an anagram of another string in the list
                pair_count += 1

                # Check if the length of the current string is at least three letters long
                if len(curr_str) >= 3:
                    # Increment the three letter count if the length of the current string is at least three letters long
                    three_letter_count += 1

# Return true if there are at least 277 pairs of anagrams in the given list; otherwise, return false
if pair_count >= 277 and three_letter_count > 0:
    return True
else:
    return False
