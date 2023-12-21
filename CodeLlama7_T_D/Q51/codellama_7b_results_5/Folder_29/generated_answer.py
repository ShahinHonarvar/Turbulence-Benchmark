
def if_contains_anagrams(my_list):
    # Define a function to check if two strings are anagrams of each other
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    # Initialize a counter for the number of pairs of anagrams in the list
    pair_counter = 0
    # Iterate over all possible pairs of strings in the list
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            # Check if the current pair of strings is an anagram
            if is_anagram(my_list[i], my_list[j])):
                # Increment the counter for the number of pairs of anagrams in the list
                pair_counter += 1
    # Return True if there are at most 318 pairs of anagrams in the list; otherwise, return False
    return pair_counter <= 318
