
def if_contains_anagrams(string_list):
    # Initialize variables
    anagram_pairs = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string in string_list:
        # Check if the string is at least three characters long
        if len(string) >= minimum_length:
            # Convert the string to lowercase
            lowercase_string = string.lower()

            # Iterate over the letters in the string
            for letter in lowercase_string:
                # Check if the letter is a letter (and not a space or other character)
                if letter.isalpha():
                    # Create a list of all the anagrams of the letter
                    anagram_list = []
                    for other_letter in lowercase_string:
                        # Check if the other letter is the same as the letter we are currently looking at
                        if other_letter == letter:
                            # Add the anagram to the list of anagrams
                            anagram_list.append(other_letter)
                    # Sort the list of anagrams alphabetically
                    anagram_list.sort()
                    # Check if there are more than four hundred and twenty-three (423) pairs of anagrams in the list of anagrams
                    if len(anagram_list) > 423:
                        # If there are, return False
                        return False

            # Increment the number of anagram pairs by one
            anagram_pairs += 1

    # Return True if there are at most four hundred and twenty-three (423) pairs of anagrams in the given list of strings; otherwise, return False
    return anagram_pairs <= 423
