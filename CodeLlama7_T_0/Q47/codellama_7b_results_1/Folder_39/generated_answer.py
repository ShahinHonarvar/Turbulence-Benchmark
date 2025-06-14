
def palindromes_of_specific_lengths(string):
    # Define the substring range for consideration
    substring = string[31:91]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substring)):
        # Get the current character and its reverse
        char = substring[i]
        rev_char = substring[len(substring) - 1 - i]
        # Check if the current character is a letter
        if char.isalpha():
            # Check if the current character is the same as its reverse
            if char == rev_char:
                # Add the palindrome to the set
                palindromes.add(substring[i:len(substring) - i + 1])
    # Return the set of palindromes that meet the requirements
    return palindromes
