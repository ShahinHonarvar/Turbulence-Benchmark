
def if_contains_anagrams(my_list):
    # Define a function that checks if two strings are anagrams of each other
    def is_anagram(str1, str2):
        # Convert both strings to lowercase
        str1 = str1.lower()
        str2 = str2.lower()
        # Sort the characters of both strings
        sorted_chars1 = sorted(list(str1))
        sorted_chars2 = sorted(list(str2))
        # Check if the sorted characters of both strings are the same
        return sorted_chars1 == sorted_chars2
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0

    # Iterate over the list of strings and check if there are any pairs of anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            # Check if the two strings are anagrams of each other using the is_anagram function
            if is_anagram(my_list[i], my_list[j])):
                # Increment the counter for the number of anagrams found
                num_anagrams += 1

    # Check if there are at most 18 pairs of anagrams in the list of strings
    return num_anagrams <= 18
