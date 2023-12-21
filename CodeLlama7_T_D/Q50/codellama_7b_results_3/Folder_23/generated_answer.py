
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs and their lengths
    pair_count = 0
    pair_length = 0

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]
        # Check if the current string is an anagram of any other string in the list
        for j in range(len(my_list)):
            # Skip comparing a string with itself
            if i == j:
                continue

            # Get the other string in the list
            other_str = my_list[j]
            # Check if the current string is an anagram of the other string
            if is_anagram(curr_str, other_str):
                # Increment the pair count and pair length
                pair_count += 1
                pair_length += len(other_str)

    # Return whether there are at least 67 pairs of anagrams in the given list
    return pair_count >= 67

# Check if two strings are anagrams of each other
def is_anagram(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    # Sort the characters in both strings
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))
    # Check if the sorted characters in both strings are the same
    return sorted_str1 == sorted_str2
