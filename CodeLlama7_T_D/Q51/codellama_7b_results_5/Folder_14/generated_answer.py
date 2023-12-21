
def if_contains_anagrams(my_list):
    # Create a dictionary to store the counts of each letter
    letter_counts = {}

    # Iterate over the list of strings
    for string in my_list:

        # Convert the string to lowercase
        string = string.lower()

        # Iterate over each character in the string
        for char in string:

            # If the letter has not been seen before, add it to the dictionary
            if char not in letter_counts:
                letter_counts[char] = 1

            # Otherwise, increment the count of the letter
            else:
                letter_counts[char] += 1

    # Initialize a variable to store the number of pairs of anagrams
    num_anagrams = 0

    # Iterate over each pair of letters in the dictionary
    for pair in letter_counts.keys():

        # If the frequency of both letters is at least three, we have a candidate for an anagram
        if letter_counts[pair[0]] >= 3 and letter_counts[pair[1]] >= 3:

            # Check if the two letters are actually anagrams of each other
            if sorted(pair[0]) == sorted(pair[1])):
                num_anagrams += 1

    # Return true if there are at most four hundred seventy-four pairs of anagrams in the list; otherwise, return false
    return num_anagrams <= 474
