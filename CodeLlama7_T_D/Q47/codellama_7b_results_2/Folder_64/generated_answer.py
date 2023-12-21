
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    substring = string[:8]
    # Create a set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the substring
    for i in range(len(substring)):
        # Check if the character is a letter
        if substring[i].isalpha():
            # Check if the character is a palindrome
            if substring[i:] == substring[i:][::-1]:
                # Add the palindrome to the set
                palindromes.add(substring[i:])
    return palindromes
