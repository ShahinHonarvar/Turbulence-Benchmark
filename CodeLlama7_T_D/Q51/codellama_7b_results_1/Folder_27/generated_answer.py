
def if_contains_anagrams(my_list):
    # Define a function to check if two strings are anagrams
    def is_anagram(str1, str2):
        # Convert the strings to lowercase
        str1 = str1.lower()
        str2 = str2.lower()
        # Sort the characters of each string
        sorted_str1 = "".join(sorted(str1))
        sorted_str2 = "".join(sorted(str2))
        # Return True if the strings are anagrams, False otherwise
        return sorted_str1 == sorted_str2
    # Initialize a variable to count the number of anagrams in the list
    num_anagrams = 0
    # Iterate over the elements of the list
    for i in range(len(my_list)):
        # Check if the current element is an anagram of any other element in the list
        for j in range(i + 1, len(my_list)):
            if is_anagram(my_list[i], my_list[j]):
                num_anagrams += 1
    # Return True if there are at most 113 pairs of anagrams in the list, False otherwise
    return num_anagrams <= 113
