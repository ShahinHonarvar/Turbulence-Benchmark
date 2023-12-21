
def palindromes_of_specific_lengths(string):
    # Define the substring range to search for palindromes
    substring = string[31:74]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the substring
    for i in range(len(substring)):
        # Get the current character and its corresponding reverse character
        char = substring[i]
        rev_char = substring[len(substring) - 1 - i]
        # Check if the character is a letter (uppercase or lowercase)
        if char.isalpha():
            # Check if the reverse character is also a letter (uppercase or lowercase)
            if rev_char.isalpha():
                # Check if the current character and its reverse character are the same
                if char == rev_char:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substring[i:len(substring) - i + 1])
    return palindromes
