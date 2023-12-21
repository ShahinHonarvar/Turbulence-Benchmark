
def if_contains_anagrams(strings):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the input list
    for string in strings:

        # Convert the current string to lowercase
        lowercase_string = string.lower()

        # Sort the characters of the current string
        sorted_characters = "".join(sorted(lowercase_string))

        # If the sorted characters have been seen before, increase the anagram count
        if sorted_characters in anagram_counts:
            anagram_counts[sorted_characters] += 1

        # Otherwise, add a new entry to the dictionary with an initial count of 1
        else:
            anagram_counts[sorted_characters] = 1

    # Loop through each key in the anagram counts dictionary
    for sorted_characters in anagram_counts:

        # If the current anagram count is greater than 98, return false immediately
        if anagram_counts[sorted_characters] > 98:
            return False

    # If all anagram counts are less than or equal to 98, return true
    return True
