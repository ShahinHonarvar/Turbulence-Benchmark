
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Sort the letters in the string
        sorted_letters = "".join(sorted(lowercase_string))

        # Check if the sorted letters are already in the dictionary
        if sorted_letters in anagram_counts:
            # Increment the count for this anagram
            anagram_counts[sorted_letters] += 1

        else:
            # Add a new entry to the dictionary with a count of 1
            anagram_counts[sorted_letters] = 1

    # Loop through each pair of anagrams in the dictionary
    for sorted_letters, count in anagram_counts.items():
        # Check if there are at most 25 pairs of anagrams
        if count > 25:
            return False

    # If we reach this point, then there are at most 25 pairs of anagrams in the list
    return True
