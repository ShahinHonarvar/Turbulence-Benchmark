
def palindromes_of_specific_lengths(string):
    # Define the substring range for finding palindromes
    substr_start = 43
    substr_end = 95
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring range
    for i in range(substr_start, substr_end + 1):
        # Check if the current character is a letter (uppercase or lowercase)
        if string[i].isalpha():
            # Convert the current character to uppercase
            char = string[i].upper()
            # Iterate over each length of palindrome between 18 and 47 (both inclusive)
            for len in range(18, 48):
                # Check if the current length is greater than or equal to the length of the substring range
                if len >= substr_end - substr_start + 1:
                    break
                # Check if the current length is greater than or equal to the length of the palindrome
                if len >= len(char * 2) - 1:
                    # Check if the current character is in the middle of the palindrome
                    if char == string[i + len // 2]:
                        # Add the current palindrome to the set
                        palindromes.add(char * (len + 1) // 2))
    return palindromes
