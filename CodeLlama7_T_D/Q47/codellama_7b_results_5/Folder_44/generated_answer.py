
def palindromes_of_specific_lengths(string):
    # Create a substring of the input string from index 18 to index 98 (inclusive)
    substring = string[18:98]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Get the character at index i
        char = substring[i]
        # Check if the character is a letter (not a whitespace or a symbol)
        if char.isalpha():
            # Get the length of the palindrome starting from index i
            palindrome_length = len(substring[i:]) - len(substring[:i])
            # Check if the palindrome length is between 31 and 51 (both inclusive)
            if 31 <= palindrome_length <= 51:
                # Get the palindrome starting from index i
                palindrome = substring[i:i + palindrome_length]
                # Check if the palindrome is a case-insensitive match for the input string
                if palindrome.lower() == string.lower():
                    # Add the palindrome to the set of palindromes
                    palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
