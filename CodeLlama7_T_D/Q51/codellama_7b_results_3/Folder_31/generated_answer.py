
def if_contains_anagrams(my_list):
    # Define the English alphabet as a set
    english_alphabet = set('abcdefghijklmnopqrstuvwxyz')
    # Initialize the counter for anagram pairs to 0
    anagram_pair_counter = 0
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if the string contains only English letters
        if set(lowercase_string) == english_alphabet:
            # Split the string into individual letters
            letter_list = list(lowercase_string)
            # Initialize a flag to check for anagrams
            found_anagram = False

            # Iterate over the letters in the string
            for i in range(len(letter_list)):
                # Check if there are any other occurrences of the current letter in the string
                if lowercase_string.count(letter_list[i]) > 1:
                    # If there are, set the flag to True and break out of the loop
                    found_anagram = True
                    break

            # If the flag is still False after checking all the letters, then the string does not contain any anagrams
            if not found_anagram:
                # Increment the counter for non-anagram strings
                anagram_pair_counter += 1

    # Return True if there are at most 65 pairs of anagrams in the given list; otherwise, return False
    return anagram_pair_counter <= 65
