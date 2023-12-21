
def if_contains_anagrams(my_list):
    # Define a function to check if two strings are anagrams of each other
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    # Initialize a counter for the number of pairs of anagrams
    pair_count = 0
    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        str1 = my_list[i]
        # Iterate over the remaining strings
        for j in range(i+1, len(my_list)):
            # Get the other string
            str2 = my_list[j]
            # Check if the two strings are anagrams of each other
            if is_anagram(str1, str2):
                # Increment the counter for the number of pairs of anagrams
                pair_count += 1
    # Return True if there are at most 36 pairs of anagrams in the given list; otherwise, return False
    return pair_count <= 36
