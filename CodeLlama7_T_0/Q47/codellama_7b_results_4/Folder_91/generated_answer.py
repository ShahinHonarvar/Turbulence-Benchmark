
def palindromes_of_specific_lengths(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(len(string)):
        # Get the substring starting from index i to index 10 (both inclusive)
        substring = string[i:11]
        # Loop through each length of palindrome between 3 and 5 (both inclusive)
        for length in range(3, 6):
            # Get the substring of the specified length
            substr_length = substring[:length]
            # Check if the substring is a palindrome
            if substr_length == substr_length[::-1]:
                # Add the palindrome to the set
                palindromes.add(substr_length)
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
