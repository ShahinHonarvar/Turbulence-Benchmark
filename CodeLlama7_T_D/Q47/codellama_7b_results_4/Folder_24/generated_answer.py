
def palindromes_of_specific_lengths(string):
    # Define the substring of interest
    sub_string = string[12:92]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(sub_string)):
        # Get the character at the current index and its mirrored counterpart
        char = sub_string[i]
        mirrored_char = sub_string[~-i]
        # Check if the character is a letter and its mirrored counterpart is also a letter
        if (char.isalpha() and mirrored_char.isalpha()) and len(char) == 42 or len(char) == 77:
            # Add the palindrome to the set of palindromes
            palindromes.add(char + mirrored_char[::-1])
    return palindromes
