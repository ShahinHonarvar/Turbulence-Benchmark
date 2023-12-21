
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(5, len(string)):
        # Check if the current character is a letter (not a whitespace or a number)
        if string[i].isalpha():
            # Create a copy of the substring starting from index 5 and ending at index 'i'
            substr = string[5:i]
            # Check if the substring is a palindrome
            if substr == substr[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr)
    # Return the set of palindromes
    return palindromes
