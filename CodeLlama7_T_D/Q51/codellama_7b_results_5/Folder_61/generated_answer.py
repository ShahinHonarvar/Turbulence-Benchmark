
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a palindrome
        if lowercase_string == lowercase_string[::-1]:
            # If the string is a palindrome, remove it from the list
            my_list.remove(string)

    # Iterate over the list of strings again
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a palindrome
        if lowercase_string == lowercase_string[::-1]:
            # If the string is a palindrome, count it as an anagram
            anagram_counts[string] = 1

    # Iterate over the list of strings again
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is a palindrome
        if lowercase_string == lowercase_string[::-1]:
            # If the string is a palindrome, count it as an anagram
            anagram_counts[string] += 1

    # Iterate over the dictionary of anagram counts
    for key, value in anagram_counts.items():
        # Check if there are at most 50 pairs of anagrams in the given list
        if value > 2:
            return False

    return True
