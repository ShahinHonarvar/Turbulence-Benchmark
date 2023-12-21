
def if_contains_anagrams(my_list):
    # Define a function to check for anagrams
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    # Initialize a counter for the number of pairs of anagrams found
    num_pairs = 0
    # Iterate over each pair of strings in the list
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            # Check if the two strings are anagrams
            if is_anagram(my_list[i], my_list[j])):
                # Increment the counter if a pair of anagrams is found
                num_pairs += 1
    # Return True if there are at most 54 pairs of anagrams in the list, otherwise return False
    return num_pairs <= 54
