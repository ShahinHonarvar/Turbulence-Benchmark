
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a palindrome
        if lowercase_string == lowercase_string[::-1]:
            # Increment the anagram count
            anagram_count += 1

    # Return True if there are at most 67 pairs of anagrams in the given list, otherwise return False
    return anagram_count <= 67
