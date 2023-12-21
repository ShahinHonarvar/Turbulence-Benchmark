
def if_contains_anagrams(my_list):
    # Define a function to check if two strings are anagrams
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    # Initialize a counter for the number of pairs of anagrams
    num_pairs = 0
    # Iterate over each string in the list
    for i in range(len(my_list)):
        # Get the current string
        str1 = my_list[i]
        # Iterate over each remaining string in the list
        for j in range(i + 1, len(my_list))):
            # Get the current string
            str2 = my_list[j]
            # Check if the two strings are anagrams
            if is_anagram(str1, str2) and len(str1) >= 3:
                num_pairs += 1
    # Return whether there are at least 10 pairs of anagrams in the list
    return num_pairs >= 10
