
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
                    # If there are more than 29 pairs of anagrams, return False
                    if anagram_count > 29:
                        return False
    # If there are no strings in the list that are at least three letters long, return False
    if not three_or_more_letters:
        return False

    # If there are no more than 29 pairs of anagrams, return True
    if anagram_count <= 29:
        return True
