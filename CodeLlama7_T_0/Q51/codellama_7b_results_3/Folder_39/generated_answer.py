
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is at least three characters long
        if len(lowercase_string) >= 3:
            # Create a list of all the letters in the string
            letter_list = [char for char in lowercase_string]

            # Sort the list of letters
            sorted_letter_list = sorted(letter_list)

            # Join the sorted list of letters into a single string
            anagram = "".join(sorted_letter_list)

            # Increment the count for this anagram
            if anagram in anagram_counts:
                anagram_counts[anagram] += 1

            else:
                anagram_counts[anagram] = 1

    # Check if there are at most 257 pairs of anagrams in the list
    return len(anagram_counts) <= 257
