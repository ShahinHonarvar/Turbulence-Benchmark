
def palindrome_of_length_at_least_n(string, n):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the string
    for i in range(len(string)):
        # Check if the character is a letter
        if string[i].isalpha():
            # Get the substring starting from the current character and ending at the end of the string
            substr = string[i:].lower()
            # Iterate over each palindrome in the substring
            for j in range(len(substr) - 1, -1, -1):
                # Check if the palindrome has a length greater than or equal to n
                if len(substr[:j+1]) >= n:
                    # Add the palindrome to the set of palindromes
                    palindromes.add(substr[:j+1])
    # Return the set of palindromes
    return palindromes
