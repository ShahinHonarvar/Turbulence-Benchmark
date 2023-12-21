
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []
    # Loop through each character in the string starting from index 37 (inclusive) and ending at index 57 (exclusive)
    for i in range(37, 57):
        # Check if the current character is a vowel letter (A, E, I, O, or U)
        if my_string[i].isalpha() and my_string[i].lower() in ["a", "e", "i", "o", "u"]:
            # If it's greater than the character * and smaller than or equal to character P
            if my_string[i] > "*":
                if my_string[i] <= "P":
                    # Add the current character to the list of vowel characters
                    vowel_list.append(my_string[i])
    return vowel_list
