
def if_contains_anagrams(my_list):
    # Create a dictionary to store the number of anagrams for each length
    anagram_counts = {}

    # Iterate over the list of strings and count the number of anagrams for each length
    for string in my_list:
        # Convert the string to lowercase
        string = string.lower()

        # Get the length of the string
        length = len(string)

        # Check if the length is at least three and if it is not longer than 318 characters
        if length >= 3 and length <= 318:
            # Add one to the number of anagrams for this length
            anagram_counts[length] = anagram_counts.get(length, 0) + 1

    # Iterate over the dictionary of anagram counts and check if there are at most 318 pairs of anagrams for each length
    for length in anagram_counts:
        number_of_anagrams = anagram_counts[length]

        # If there are at least three anagrams for this length, then return false
        if number_of_anagrams >= 3:
            return False

    # If all the lengths have at most 318 pairs of anagrams, then return true
    return True
