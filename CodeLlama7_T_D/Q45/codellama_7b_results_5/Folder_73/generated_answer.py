
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(3, len(string) + 1):
        # Check if the substring starting from index 3 has at least 3 characters
        if len(string[i - 2:i]) < 3:
            continue

        # Create a palindrome by reversing the substring starting from index 3
        palindrome = string[i - 2:i][::-1]
        # Check if the palindrome has at least 3 characters
        if len(palindrome) < 3:
            continue

        # Add the palindrome to the set of palindromes
        palindromes.add(palindrome)
    # Return the set of palindromes
    return palindromes
