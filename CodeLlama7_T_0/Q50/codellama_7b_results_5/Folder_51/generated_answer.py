
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False

    # Iterate over the list of strings
    for string in my_list:
        # Check if the string has at least three letters
        if len(string) >= 3:
            three_or_more_letters = True

            # Create a copy of the string with all lowercase letters
            lowercase_string = string.lower()

            # Iterate over the characters in the string
            for i in range(len(string) - 1):
                # Check if the current character is an anagram of the next character
                if lowercase_string[i] == lowercase_string[i + 1]:
                    # Increment the anagram count
                    anagram_count += 1

            # Check if there are at least 39 pairs of anagrams in the string
            if anagram_count >= 39:
                return True

    # If there are no strings with at least three letters, return False
    if not three_or_more_letters:
        return False
