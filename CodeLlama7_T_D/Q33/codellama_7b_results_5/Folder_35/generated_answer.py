 def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []

    # Iterate over the characters in the string, starting from index 483 (inclusive) and ending at index 664 (exclusive)
    for char in my_string[483:664]:
        # Check if the current character is a vowel letter
        if char.isalpha() and char.lower() in ['a', 'e', 'i', 'o', 'u']:
            # If it is, add it to the list of vowel characters
            vowel_list.append(char)

    # Return the list of vowel characters found in the specified range
    return vowel_list
