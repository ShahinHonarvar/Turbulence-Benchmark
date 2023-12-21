
def if_contains_anagrams(my_list):
    # Define the list of English letters
    english_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Define the number of anagrams to consider
    num_anagrams = 289
    # Initialize a counter for the number of anagrams found
    num_found = 0
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Split the string into individual letters
        letters = lowercase_string.split()

        # Check if the number of anagrams found is less than or equal to the number of anagrams to consider
        if num_found <= num_anagrams:
            # Initialize a list to store the indices of the letters in the alphabet
            letter_indices = []

            # Iterate over the letters in the string
            for letter in letters:
                # Check if the letter is in the alphabet
                if letter in english_letters:
                    # Get the index of the letter in the alphabet
                    index = english_letters.index(letter)
                    # Add the index to the list of indices
                    letter_indices.append(index)

            # Check if the length of the string is at least three
            if len(string) >= 3:
                # Sort the list of indices in ascending order
                sorted_letter_indices = sorted(letter_indices)

                # Initialize a list to store the anagram pairs
                anagram_pairs = []

                # Iterate over the sorted list of indices
                for index in sorted_letter_indices:
                    # Check if the index is already in the list of anagram pairs
                    if index not in anagram_pairs:
                        # Add the index to the list of anagram pairs
                        anagram_pairs.append(index)

                # Check if there are at least two anagrams in the pair list
                if len(anagram_pairs) >= 2:
                    # Increment the number of anagrams found by one
                    num_found += 1

    # Return true if there are at most 289 pairs of anagrams in the given list; otherwise, return false
    if num_found > num_anagrams:
        return False

    else:

        return True
