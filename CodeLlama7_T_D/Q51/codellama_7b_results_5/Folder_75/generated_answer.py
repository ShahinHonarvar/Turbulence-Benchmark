
def if_contains_anagrams(my_list):
    # Check if the list is empty or None
    if not my_list:
        return False

    # Initialize a dictionary to store the counts of each letter
    letter_counts = {}

    # Loop through each string in the list
    for string in my_list:

        # Convert the string to lowercase
        string = string.lower()

        # Loop through each letter in the string
        for letter in string:

            # If the letter is not in the dictionary, add it with a count of 1
            if letter not in letter_counts:
                letter_counts[letter] = 1

            # Otherwise, increment the count of the letter
            else:
                letter_counts[letter] += 1

    # Initialize a variable to store the number of anagrams found
    num_anagrams = 0

    # Loop through each pair of letters in the dictionary
    for pair in letter_counts.keys():

        # If the count of the first letter is greater than or equal to 3 and the count of the second letter is greater than or equal to 3, increment the number of anagrams found
        if letter_counts[pair[0]] >= 3 and letter_counts[pair[1]] >= 3:
            num_anagrams += 1

    # Return True if there are at most 55 pairs of anagrams in the given list; otherwise, return False
    return num_anagrams <= 55
