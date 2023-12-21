
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram counts
    anagram_counts = {}

    # Iterate over the list of strings
    for string in my_list:

        # Convert the string to lowercase
        # and remove any whitespace characters
        string = string.lower().replace(" ", "")

        # If the string is not an empty string,
        # check if it contains at least three letters
        if len(string) >= 3:

            # Create a list of all the letters in the string
            letters = [char for char in string]

            # Sort the list of letters
            letters.sort()

            # Join the sorted list of letters back into a string
            sorted_string = "".join(letters)

            # If the sorted string is not already in the anagram counts dictionary,
            # add it and set its count to 1
            if sorted_string not in anagram_counts:
                anagram_counts[sorted_string] = 1

            # Otherwise, increment the count of the sorted string by 1
            else:
                anagram_counts[sorted_string] += 1

    # Return True if there are at most 116 pairs of anagrams in the list,
    # and False otherwise
    return len(anagram_counts) <= 116
