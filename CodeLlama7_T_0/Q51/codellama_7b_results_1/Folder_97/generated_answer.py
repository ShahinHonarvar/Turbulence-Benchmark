
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False
    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()
        # Check if the string is at least three letters long
        if len(lowercase_string) >= 3:
            three_or_more_letters = True
            # Create a list of all the letters in the string
            letter_list = [char for char in lowercase_string]
            # Sort the list of letters
            sorted_letter_list = sorted(letter_list)
            # Check if there are any anagrams in the list
            for i in range(len(sorted_letter_list) - 1):
                if sorted_letter_list[i] == sorted_letter_list[i + 1]:
                    anagram_count += 1
                    # If there are at least 18 pairs of anagrams, return False
                    if anagram_count >= 18:
                        return False
            # If there are no anagrams in the list, return True
            if anagram_count == 0:
                return True

# If the function is called with a list of strings that does not contain at least three letters, return False
if not all(len(string) >= 3 for string in my_list)):
    return False
