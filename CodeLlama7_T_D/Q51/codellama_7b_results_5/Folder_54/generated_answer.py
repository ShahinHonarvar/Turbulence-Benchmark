
def if_contains_anagrams(my_list):
    # Define a function to check for anagrams
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        str1 = my_list[i]
        # Check if the current string is a palindrome
        if str1 == str1[::-1]:
            # Increment the counter for the number of anagrams found
            num_anagrams += 1
    # Check if there are at most 39 pairs of anagrams in the given list
    return num_anagrams <= 39
