
def if_contains_anagrams(my_list):
    # Define a function to check if two strings are anagrams
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    # Define a variable to count the number of anagrams in the list
    num_anagrams = 0
    # Iterate through each pair of strings in the list
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            # Check if the two strings are anagrams and increase the count if they are
            if is_anagram(my_list[i], my_list[j])):
                num_anagrams += 1
    # Return True if there are at most 48 pairs of anagrams in the list, otherwise return False
    return num_anagrams <= 48
