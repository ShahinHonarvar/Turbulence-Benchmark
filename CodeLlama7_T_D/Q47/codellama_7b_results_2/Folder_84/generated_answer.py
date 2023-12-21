
def palindromes_of_specific_lengths(string):
    # Define the substring range for finding palindromes
    substr = string[23:77]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring
    for i in range(len(substr)):
        # Define the substring starting from current index
        substr_curr = substr[i:]
        # Check if the substring is a palindrome
        if substr_curr == substr_curr[::-1]:
            # Add the palindrome to the set
            palindromes.add(substr_curr)
    # Return the set of palindromes that satisfy the requirements
    return palindromes
