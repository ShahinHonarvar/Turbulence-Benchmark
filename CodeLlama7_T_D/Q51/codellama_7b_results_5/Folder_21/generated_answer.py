
def if_contains_anagrams(my_list):
    # Check that the list is not empty
    if len(my_list) == 0:
        return False

    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a palindrome (i.e., it reads the same forward and backward)
        if lowercase_string == lowercase_string[::-1]:
            # If the string is a palindrome, then we can ignore it because we don't want to consider anagrams of palindromes
            continue

        # Create a list of all the characters in the string (i.e., the letters that are not spaces)
        characters = [char for char in lowercase_string if char != " "]

        # Sort the characters in alphabetical order
        sorted_characters = sorted(characters)

        # Join the sorted characters together to create a single string (i.e., an anagram of the original string)
        anagram = "".join(sorted_characters)

        # Check if we have already seen this anagram before
        if anagram in anagram_counts:
            # If we have seen this anagram before, then increase its count by 1
            anagram_counts[anagram] += 1

        # Otherwise, add this anagram to the dictionary with a count of 1
        else:
            anagram_counts[anagram] = 1

    # Check if there are at most 26 pairs of anagrams in the list
    return len(anagram_counts) <= 26 * 26
