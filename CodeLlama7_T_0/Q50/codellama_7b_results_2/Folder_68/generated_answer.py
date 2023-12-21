
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_chars = False
    # Iterate over the list of strings
    for string in my_list:
        # Check if the string has at least three characters
        if len(string) >= 3:
            three_or_more_chars = True
            # Create a copy of the string with all lowercase letters
            lowercase_string = string.lower()
            # Sort the characters in the string
            sorted_characters = "".join(sorted(lowercase_string))
            # Check if there are at least 9 pairs of anagrams in the list
            for other_string in my_list:
                if lowercase_string != other_string.lower():
                    # Create a copy of the other string with all lowercase letters
                    lowercase_other_string = other_string.lower()
                    # Sort the characters in the other string
                    sorted_characters_other_string = "".join(sorted(lowercase_other_string))
                    # Check if the two strings are anagrams of each other
                    if sorted_characters == sorted_characters_other_string:
                        anagram_count += 1
            # If there are at least 9 pairs of anagrams in the list, return True
            if anagram_count >= 9:
                return True
    # If there are no strings with at least three characters, return False
    if not three_or_more_chars:
        return False
