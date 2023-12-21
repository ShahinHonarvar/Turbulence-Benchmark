
def if_contains_anagrams(string_list):
    # Initialize a dictionary to keep track of anagram counts
    anagram_counts = {}

    # Iterate over the input list of strings
    for string in string_list:
        # Convert the current string to lowercase
        lowercase_string = string.lower()

        # If the current string is not a palindrome, continue to the next iteration
        if lowercase_string != lowercase_string[::-1]:
            continue

        # Split the current string into a list of individual letters
        letter_list = [letter for letter in lowercase_string]

        # Sort the list of individual letters
        sorted_letter_list = sorted(letter_list)

        # Join the sorted list of individual letters back into a single string
        anagram = ''.join(sorted_letter_list)

        # If the current anagram is already in the dictionary, increment its count
        if anagram in anagram_counts:
            anagram_counts[anagram] += 1

        # Otherwise, add it to the dictionary with a count of one
        else:
            anagram_counts[anagram] = 1

    # Iterate over the dictionary of anagram counts
    for anagram in anagram_counts:
        # If the current anagram has more than 18 pairs, return false
        if anagram_counts[anagram] > 18:
            return False

    # Otherwise, all anagrams have at most 18 pairs, so return true
    return True
