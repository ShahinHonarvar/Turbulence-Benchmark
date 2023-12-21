
def if_contains_anagrams(my_list):
    # Define a function to determine if two strings are anagrams
    def is_anagram(str1, str2):
        # Convert both strings to lowercase
        str1 = str1.lower()
        str2 = str2.lower()
        # Sort the characters in each string
        sorted_str1 = "".join(sorted(str1))
        sorted_str2 = "".join(sorted(str2))
        # Check if the sorted strings are equal
        return sorted_str1 == sorted_str2
    # Initialize a counter variable to keep track of the number of anagrams found
    num_anagrams = 0
    # Iterate over each pair of strings in the input list
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            # Check if the current pair of strings are anagrams
            if is_anagram(my_list[i], my_list[j])):
                # Increment the counter variable if the current pair of strings are anagrams
                num_anagrams += 1
    # Return True if there are at least 36 pairs of anagrams in the input list, otherwise return False
    return num_anagrams >= 36
